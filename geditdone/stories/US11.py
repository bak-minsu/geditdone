from geditdone.gedcom_objects import GedcomError

def no_bigamy(parser, db):
    """Throws an error when poligamy is found"""
    errors = []
    
    def get_intervals_from_duplicates(duplicates, wife_or_husband):
        intervals = []
        for index, duplicate in duplicates.items():
            if duplicate:
                family_object = db.families.iloc[index]
                interval = {
                            "ID": eval("db.families.iloc[index].{}_id".format(wife_or_husband)),
                            "married": family_object.married, 
                            "divorced": family_object.divorced,
                            "reference": family_object.reference,
                            }
                intervals.append(interval)
        return intervals

    def intervals_intersect(interval1, interval2):
        # If both marriages never divorced, then poligamy
        if interval1["divorced"] == None and interval2["divorced"] == None:
            return True
        # If one of the marriages divorced but the other did not
        elif interval1["divorced"] == None or interval2["divorced"] == None:
            if interval1["divorced"] == None and interval1["married"] < interval2["divorced"]:
                return True
            elif interval2["divorced"] == None and interval2["married"] < interval1["divorced"]:
                return True
        # If both divorced at sometime
        else:
            # If interval 1 got married first
            if interval1["married"] < interval2["married"] and interval2["married"] < interval1["divorced"]:
                return True
            # If interval 2 got married first
            elif interval2["married"] < interval1["married"] and interval1["married"] < interval2["divorced"]:
                return True
        return False
    
    def poligamy_exists(intervals):
        for i, interval_outer in enumerate(intervals):
            ID_outer = interval_outer["ID"]
            for interval_inner in intervals[i+1:]:
                if interval_inner["ID"] == ID_outer and intervals_intersect(interval_outer, interval_inner):
                    individual = db.individuals[db.individuals.ID == ID_outer].iloc[0].reference
                    family1 = interval_inner["reference"].id
                    family2 = interval_outer["reference"].id
                    errorMessage = f'Bigamy between Family {family1} and Family {family2}'
                    errors.append(GedcomError(GedcomError.ErrorType.error, 'US11', individual, errorMessage))

    fam_df = db.families
    husband_duplicates = fam_df.duplicated(subset=["husband_id"], keep=False)
    wife_duplicates = fam_df.duplicated(subset=["wife_id"], keep=False)

    husband_intervals = get_intervals_from_duplicates(husband_duplicates, "husband")
    wife_intervals = get_intervals_from_duplicates(wife_duplicates, "wife")
    poligamy_exists(husband_intervals)
    poligamy_exists(wife_intervals)

    return errors
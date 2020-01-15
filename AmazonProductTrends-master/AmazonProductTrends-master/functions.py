import pandas as pd

def cleanData():
    import pandas as pd

    """Docstring: clean data and aggregate all three datasources. Returns just one dataframe from all three csv files combined and cleaned"""

    data = "1429_1.csv"
    df = pd.read_csv(data)

    df = df.drop(["asins", "keys","manufacturer", "reviews.didPurchase", "reviews.id", "reviews.sourceURLs", "reviews.userCity", "reviews.userProvince", "reviews.numHelpful" ], axis = 1)
    df.columns = ["ID", "Name", "Brand", "Category", "Review Date", "Date Added", "Date Seen", "Recommendation", "Rating", "Review", "Review Title", "Username"]
    df = df.drop("Date Added", axis = 1)

    data1 = "Datafiniti_Amazon_Consumer_Reviews_of_Amazon_Products_May19.csv"

    df1 = pd.read_csv(data1, header = 0)
    data2= "Datafiniti_Amazon_Consumer_Reviews_of_Amazon_Products.csv"
    df2 = pd.read_csv(data2, header = 0)
    cols = ['id', 'dateAdded', 'dateUpdated', 'name', 'asins', 'brand',
           'categories', 'primaryCategories', 'imageURLs', 'keys', 'manufacturer',
           'manufacturerNumber', 'reviews.date',
           'reviews.dateSeen', 'reviews.dateAdded', 'reviews.doRecommend', 'reviews.id',
           'reviews.numHelpful', 'reviews.rating', 'reviews.sourceURLs',
           'reviews.text', 'reviews.title', 'reviews.username', 'sourceURLs']

    df1.columns = cols
    df2.columns = cols
    combined_data = pd.concat([df1, df2])

    combined_data = combined_data.drop(["asins", "keys","manufacturer", "reviews.id", "imageURLs", "manufacturerNumber", "dateUpdated", "primaryCategories", "reviews.numHelpful", "sourceURLs", "reviews.sourceURLs" ], axis = 1)
    combined_data.columns = ["ID","Date Added", "Name", "Brand", "Category", "Review Date" , "Date Seen","Date Added", "Recommendation", "Rating", "Review", "Review Title", "Username"]
    combined_data = combined_data[["ID", "Name", "Brand", "Category","Review Date", "Date Added", "Date Seen", "Recommendation", "Rating", "Review", "Review Title", "Username"]]
    combined_data = combined_data.drop("Date Added", axis = 1)
    full_data = pd.concat([df, combined_data])
    full_data = full_data.reset_index()
    full_data = full_data.drop_duplicates(subset='Review', keep='first')

    return full_data

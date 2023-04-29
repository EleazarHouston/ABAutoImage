import json
import matplotlib

def calcStats():
    with open('private/imageCategories.json') as f:
        categories = json.load(f)
    with open('data/UserData.json') as f:
        userData = json.load(f)
    userFeatureStats = {}
    featureStats = {}

    for category, features in categories.items():
        featureStats[category] = {}
        for feature in features:
            featureStats[category][feature] = {'total': 0, 'preferred': 0}
    
    for userID, userPrefs in userData.items():
        userFeatureStats[userID] = {}
        for pair in userPrefs['pairs']:
            image1Features = pair['image1']
            image2Features = pair['image2']
            preference = pair['preference']

            for feature in image1Features + image2Features:
                for category, features in categories.items():
                    if feature in features:
                        if category not in userFeatureStats[userID]:
                            userFeatureStats[userID][category] = {}
                        if feature not in userFeatureStats[userID][category]:
                            userFeatureStats[userID][category][feature] = {'total': 0, 'preferred': 0}

                        featureStats[category][feature]['total'] += 1
                        userFeatureStats[userID][category][feature]['total'] += 1

                        if preference == 'image1' and feature in image1Features or preference == 'image2' and feature in image2Features:
                            featureStats[category][feature]['preferred'] += 1
                            userFeatureStats[userID][category][feature]['preferred'] += 1
    with open('data/UserPreferenceStats.json', 'w') as f:
        json.dump(userFeatureStats, f)
    
    with open('data/GlobalFeatureStats.json', 'w') as f:
        json.dump(featureStats, f)
    
    for userID, categoriesStats in userFeatureStats.items():
        print(f'User {userID}:')
        for category, featuresStats in categoriesStats.items():
            print(f'  {category}:')
            for feature, stats in featuresStats.items():
                if stats['total'] > 0:
                    prefPercentage = stats['preferred'] / stats['total'] * 100
                    print(f'    {feature}: {prefPercentage:.2f}% preferred')
        print()
    
    for category, featuresStats in featureStats.items():
        print(f'GLOBAL: {category}')
        for feature, stats in featuresStats.items():
            if stats['total'] > 0:
                prefPercentage = stats['preferred'] / stats['total'] * 100
                print(f'  {feature}: {prefPercentage:.2f}% preferred')
    return userFeatureStats, featureStats
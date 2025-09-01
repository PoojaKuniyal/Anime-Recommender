from utils.helpers import *
from config.paths_config import *
from pipeline.prediction_pipeline import hybrid_recommendation


# similar_user = find_similar_users(11880, USER_WEIGHTS_PATH,USER2USER_ENCODED,USER2USER_DECODED)
# # print(similar_user)

# user_pref = get_user_preferences(11880,RATING_DF,DF)
# # print(user_pref)

# print(get_user_recommendations(similar_user,user_pref,DF, SYNOPSIS_DF,RATING_DF))
# print(hybrid_recommendation(13994))

print(find_similar_animes('Fairy Tail', ANIME_WEIGHTS_PATH, ANIME2ANIME_ENCODED, ANIME2ANIME_DECODED, DF))


# print(get_user_preferences(11880, RATING_DF, DF).head())
# print(find_similar_users(11880, USER_WEIGHTS_PATH, USER2USER_ENCODED, USER2USER_DECODED).head())

# df = pd.read_csv(DF)
# print(df.columns.tolist())
# print(df.head())

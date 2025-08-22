from tensorflow.keras.models import Model 
from tensorflow.keras.layers import Input,Embedding,Dot,Flatten,Dense,Activation,BatchNormalization
from utils.common_functions import read_yaml
from src.logger import get_logger
from src.custom_exception import CustomException

logger = get_logger(__name__)

class BaseModel:
    def __init__(self, config_path):
       try:
           self.config = read_yaml(config_path)
           logger.info("Loaded configuration from config.yaml")
       except Exception as e:
           raise CustomException("Error loading configuration",e)
    
    def RecommenderNet(self,n_users, n_anime):
        try:
            embedding_size = self.config["model"]["embedding_size"]
            user = Input(name='user', shape=[1]) #- Shape [1] means each sample is a scalar (not a sequence).

            user_embedding = Embedding(name="user_embedding", input_dim=n_users, output_dim=embedding_size)(user)
            
            anime = Input(name='anime', shape=[1])
            # - Computes the cosine similarity between user and anime embeddings
            anime_embedding = Embedding(name="anime_embedding", input_dim=n_anime, output_dim=embedding_size)(anime)

            x = Dot(name='dot_product',normalize= True, axes=2)([user_embedding, anime_embedding]) # similarity b/w user embedding and anime embedding
            x = Flatten()(x)

            x = Dense(1, kernel_initializer='he_normal')(x)
            x= BatchNormalization()(x)
            x = Activation("sigmoid")(x)

            model = Model(inputs = [user,anime], outputs=x) # we made user and anime input different so that we can pass them as input

            model.compile(loss=self.config['model']['loss'],
                          optimizer= self.config['model']['optimizer'],
                          metrics = self.config['model']['metrics']
                          )
            logger.info("Model created successfully")
            return model
        except Exception as e:
            logger.error(f"Error occurred during model architecture {e}")
            raise CustomException("Failed to create model",e)
        

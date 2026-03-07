from authx import AuthX, AuthXConfig

config = AuthXConfig(
    JWT_SECRET_KEY='MgXMlqSHxb1bUJkhE9b68BsonWMuQdJR',
    JWT_TOKEN_LOCATION=['cookies']
)

security = AuthX(config=config)

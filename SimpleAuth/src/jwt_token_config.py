from authx import AuthX, AuthXConfig

config = AuthXConfig(
    JWT_SECRET_KEY='Wql78EBy2x2SdLvO',
    JWT_TOKEN_LOCATION=['cookies']
)

auth = AuthX(config=config)
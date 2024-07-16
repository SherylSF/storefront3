from .common import *

env_name = os.getenv('ENV_NAME', 'dev')

if env_name == 'prod':
    from .prod import *
elif env_name == 'dev':
    from .dev import *
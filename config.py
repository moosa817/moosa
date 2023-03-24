from os import getenv
import os

# config Variables
template_dir = os.path.abspath('app/templates/error')
static_dir = os.path.abspath('app/public/')
log_file = 'logs/debug.log'

#secrets
debug_mode = getenv("DEBUG", True)
auth = getenv("AUTH")
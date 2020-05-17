# Ancora Imparo.
from limp.gateway import Gateway
from limp.utils import validate_attr
from limp.classes import PACKAGE_CONFIG, ATTR


config = PACKAGE_CONFIG(
	api_level='6.1',
	# Use sematic versioning for package version, so you keep package version and major corresponding to API level, while minor is increamental per new version of the package, and reset it for new API level
	version='6.1.0',
	# Define package vars. This is shared storage across packages so you can have multiple packages communicating per specific instructions defined here. You can also use this to define 'globals' dict which you can use across your modules
	# vars={
	# 	'globals':{
	# 		...
	# 	}
	# }
)

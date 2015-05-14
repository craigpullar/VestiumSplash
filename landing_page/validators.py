from django.core.validators import RegexValidator

email_regex = RegexValidator(
	regex= '/\A[^@]+@([^@\.]+\.)+[^@\.]+\z/',
	message = 'Email did not pass validation',
	code = "invalid_email"
	)

username_regex = RegexValidator(
	regex = '^[a-zA-Z0-9_]*$',
	message = 'Username did not pass validation',
	code = 'invalid_username'
	)

ip_regex =	RegexValidator(
	regex = '\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b',
	message = 'IP Address did not pass validation',
	code = 'invalid_ip_address'
	)
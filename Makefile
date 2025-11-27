install:
	@pip install -U pip
	@pip install -e .

check:
	-@echo "🔍 Checking .env file..."
	-@test -f .env || (echo "🚫 .env file is missing" && exit 1)

	-@echo "🔍 Checking SESSION variable..."
	-@grep -q "^SESSION=" .env || (echo "🚫 SESSION variable not found in .env" && exit 1)
	-@[ -n "$$(grep '^SESSION=' .env | cut -d '=' -f2)" ] || (echo "🚫 SESSION variable is empty" && exit 1)

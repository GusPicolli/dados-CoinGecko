export RAW_PATH = ../dados-CoinGecko/AWS/S3/RAW/
export WORK_PATH = ../dados-CoinGecko/AWS/S3/WORK/


terragrunt/init:
	(cd terraform && terragrunt init)

terragrunt/plan:
	(cd terraform && terragrunt plan)

terragrunt/apply:
	(cd terraform && terragrunt apply)

terragrunt/init:
	(cd terraform && terragrunt init)

terragrunt/clean:
	(cd terraform && rm -rf .terraform .terraform.lock.hcl)

requirements:
	pip install -r requirements.txt

run:
	python src/app.py

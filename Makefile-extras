LOCAL_SPEC_FILE=./build/public-api.yaml

init-venv:
	if [ ! -d ".venv" ]; then python3 -m venv .venv; fi

install: init-venv
	source .venv/bin/activate; python3 -m pip install .[dev]

test:
	source .venv/bin/activate; python3 -m pytest --junitxml=build/test_results/report.xml

check: test

speakeasy-install: # dev task, locally install the speakeasy CLI
	brew install speakeasy-api/homebrew-tap/speakeasy
	speakeasy auth login

download-public-spec: # dev task, download the current public spec, in preparation for modifying and running speakeasy-generate
	curl https://docs.goshippo.com/spec/shippoapi/public-api.yaml > $$LOCAL_SPEC_FILE

speakeasy-generate: # dev task, run the generator on a local spec.  useful for testing out changes to the spec or gen.yaml - but DO NOT commit the results of manual generation
	if [ ! -f "${LOCAL_SPEC_FILE}" ]; then \
	  echo "Error: The file '${LOCAL_SPEC_FILE}' does not exist, have you run 'make download-public-spec'?"; \
	  exit 1; \
	fi
	SPEAKEASY_FORCE_GENERATION=true speakeasy generate sdk -s ${LOCAL_SPEC_FILE} -o . -l python

speakeasy-run: # dev task, locally run the complete speakeasy workflow.  useful if the generator workflow ever fails, to replicate locally
	speakeasy run

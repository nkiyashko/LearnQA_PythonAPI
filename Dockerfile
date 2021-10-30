FROM python
WORKDIR /test_project/
COPY Requirements.txt .
RUN pip install -r Requirements.txt
ENV ENV=dev
CMD python3 -m pytest -s --alluredir=test_results/ /test_project/tests/
# 
FROM python:3.9

# 
WORKDIR /jwt-utility

# 
COPY ./requirements.txt /jwt-utility/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /jwt-utility/requirements.txt

# 
COPY ./app /jwt-utility/app

# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]


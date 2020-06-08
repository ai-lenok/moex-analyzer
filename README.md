# Analysis of Moscow Exchange Securities

A simple engine for analyzing Moscow Exchange securities

# Launch
## Bash
```shell script
main_moex_analysis.py [-h] [--security SECURITY] [--date DATE]
```
Example:
```shell script
main_moex_analysis.py --security SBER --date 2020-01-01
```

# Docker
```shell script
docker build -t <image_name> .
docker run --name <container_name> -e SECURITY=<security_name> -e DATE=<date_start> <image_name>
```

Example:
```shell script
docker build -t moex_image .
docker run --name moex -e SECURITY=MOEX -e DATE=2020-01-01 moex_image
```





# Analysis of Moscow Exchange Securities

A simple engine for analyzing Moscow Exchange securities

# Launch
## Bash
### Scheme
```shell script
main_moex_analysis.py [-h] --security SECURITY [SECURITY ...] --board BOARD 
                      [--date DATE] [--chart]
```
### Example
```shell script
main_moex_analysis.py --security MOEX SBER --board TQBR --date 2020-01-01 --chart
```
Or
```shell script
main_moex_analysis.py --security SBMX SBSP --board TQTF --date 2020-01-01 --chart
```

After that inside the `chart/` directory you can find charts with security prices.

## Docker
### Scheme
```shell script
docker build -t <image_name> .
docker run [--volume <absolume_path_to_image_dir>:/moex/chart] 
           <image_name>
           [-h] --security SECURITY [SECURITY ...] --board BOARD 
           [--date DATE] [--chart]
```

### Example
```shell script
docker build -t moex_image .
docker run moex_image --security MOEX SBER --board TQBR
```
Or
```shell script
docker build -t moex_image .
docker run --volume /home/user/moex/chart:/moex/chart moex_image \
           --security SBMX SBSP --board TQTF --date 2020-01-01 --chart
```




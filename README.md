# Moscow Exchange Securities Analyzer

A simple engine for analyzing Moscow Exchange securities

# Launch
## Python

### Prepare
```shell script
pip3 install . 
```

### Scheme
```shell script
python3 moex-analyzer [-h] --security SECURITY [SECURITY ...] --board BOARD 
                      [--date DATE] [--chart]
```
### Arguments
```shell script
  -h, --help            show this help message and exit
  -s SECURITY [SECURITY ...], --security SECURITY [SECURITY ...]
                        Security for analysis
  -b BOARD, --board BOARD
                        Board where trade security
  -d DATE, --date DATE  Date of start analysis (default: 1990-01-01)
  -c, --chart           Draw chart

```
### Example
```shell script
python3 moex-analyzer --security MOEX SBER --board TQBR --date 2020-01-01 --chart
```
Or
```shell script
python3 moex-analyzer --security SBMX SBSP --board TQTF --date 2020-01-01 --chart
```

After that inside the `chart/` directory you can find charts with security prices.

## Docker
### Scheme
```shell script
docker run [--volume <absolume_path_to_image_dir>:/moex/chart] 
           dzx912/moex-analyzer
           [-h] --security SECURITY [SECURITY ...] --board BOARD 
           [--date DATE] [--chart]
```

### Example
```shell script
docker run dzx912/moex-analyzer --security MOEX --board TQBR
```
Or
```shell script
docker run --volume ~/moex/chart:/moex/chart \
           dzx912/moex-analyzer \
           --security SBMX SBSP --board TQTF --date 2020-01-01 --chart
```
After that inside the `~/moex/chart` directory you can find charts with security prices.

# Output
## Analysis
```shell script
MOEX Day change:   -2.48%
MOEX Week change:  -6.15%
MOEX Month change: 8.61%
MOEX Year change:  23.91%
```
## Chart
<img src="https://raw.githubusercontent.com/ai-lenok/moex-analyzer/master/example/MOEX.png" alt="MOEX price chart" width="800"/>

# Docker hub
https://hub.docker.com/r/dzx912/moex-analyzer



```sql
#db에 저장하기


ERROR 3948 (42000): Loading local data is disabled; this must be enabled on both the client and server sides  

해결방법
mysql> show global variables like 'local_infile';

입력하면
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| local_infile  |  OFF  |
+---------------+-------+
mysql> set global local_infile=true;
이걸 입력하면 OFF 가  ON으로 바뀐다

mysql> exit
mysql --local_infile -u root -p

CREATE TABLE date(기간코드 VARCHAR(30), 기간 VARCHAR(30));

LOAD DATA LOCAL INFILE '/home/engineer/서울시_5대범죄_현황1.csv/seoul_crime.csv.csv'
INTO TABLE date
FIELDS TERMINATED BY ',';


에러가 발생해서 기간코드 파일의 컬럼명을 삭제하고 다시 시도해보기로 함
import pyspark.sql.functions as F
a.filter(a.col("rownumber").between(2,4)).show()
```



```
#db에 넣기 위해 컬럼명 삭제
a = spark.read.format("csv").load("새폴더/서울시_행정코드.csv")
컬럼명 삭제를 위해 header 지정 없이 csv를 불러옴

a.where( col("_c0")!=("ID")).show()
거의 모든 df들이 가지고 있는 기간코드라는 컬럼명을 조건에 이용하여 해당 문자열을 가진 행을 삭제하는 방식 사용

a.coalesce(1).write.format("csv").mode("overwrite").save("/user/engineer/서울시_지역코드1.csv")

만일의 상황에 대비하여 원래 컬럼명 백업
5대범죄 - id 기간코드 지역코드 합계 살인 강도 강간강제추행 절도 폭력
경찰관 현황 - id 기간코드 경찰서명 인원수
씨씨티비 - id 기간코드 지역코드 개수
```

```sql
##데이터 db에 저장하는 코드
#5대범죄
CREATE TABLE 5_CRIME_RATES(
ID INT PRIMARY KEY,
LOCAL_CODE INT,
TOTAL INT,
MURDER INT,
ROBBER INT,
MOLEST INT,
THEFT INT,
VIOLENCE INT
);
LOAD DATA LOCAL INFILE '/home/engineer/DB/seoul_crime.csv'
INTO TABLE 5_CRIME_RATES
FIELDS TERMINATED BY ',';


#기간코드
CREATE TABLE DATE(기간코드 INT, 기간 INT);
LOAD DATA LOCAL INFILE '/home/engineer/DB/date_code.csv'
INTO TABLE DATE
FIELDS TERMINATED BY ',';

#cctv
CREATE TABLE CCTV(
ID INT PRIMARY KEY,
LOCAL_CODE INT,
TOTAL INT
);

LOAD DATA LOCAL INFILE '/home/engineer/DB/cctv.csv'
INTO TABLE CCTV
FIELDS TERMINATED BY ',';

#유동인구 이상있음
CREATE TABLE FLOATING_POP(
ID INT PRIMARY KEY,
DATE_CODE INT,
LOCAL_CODE INT,
TOTAL INT,
MAX_DAY INT,
MIN_DAY INT,
DAY_TIME INT,
NIGHT_TIME INT,
MAX_MOVE_PEOPLE INT,
LOCAL_MOVE_PEOPLE INT
);

LOAD DATA LOCAL INFILE '/home/engineer/DB/floating_pop.csv'
INTO TABLE FLOATING_POP
FIELDS TERMINATED BY ',';

#유흥업소
CREATE TABLE KARAOKE(
ID INT PRIMARY KEY,
LOCAL_CODE INT,
DATE_CODE INT,
AUTH_DATE INT,
ADDR VARCHAR(40)
);

LOAD DATA LOCAL INFILE '/home/engineer/DB/karaoke.csv'
INTO TABLE KARAOKE
FIELDS TERMINATED BY ',';

#지역코드
CREATE TABLE LOCATION(
LOCAL_CODE INT PRIMARY KEY,
LOCAL_NAME VARCHAR(5)
);

LOAD DATA LOCAL INFILE '/home/engineer/DB/loc_code.csv'
INTO TABLE LOCATION
FIELDS TERMINATED BY ',';

#경찰관 이상
CREATE TABLE POLICE_OFFICER(
ID INT PRIMARY KEY,
NAME VARCHAR(20),
DATE_CODE INT
);

LOAD DATA LOCAL INFILE '/home/engineer/DB/police_man.csv'
INTO TABLE POLICE_OFFICER
FIELDS TERMINATED BY ',';

#인구밀도
CREATE TABLE POPULATION_DENSITY(
ID INT PRIMARY KEY,
DATE_CODE INT,
POPULATION INT,
AREA INT,
DENSITY INT
);

LOAD DATA LOCAL INFILE '/home/engineer/DB/pop_den1.csv'
INTO TABLE POPULATION_DENSITY
FIELDS TERMINATED BY ',';
```







SELECT LOCAL_NAME,KARAOKE FROM LOCATION A JOIN KARAOKE B ON A.LOCAL_CODE = B.LOCAL_CODE;

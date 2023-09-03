DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
POSITIVEINCREASE=$(echo $DATA | jq '.[0].positiveIncrease')
NEGATIVE=$(echo $DATA | jq '.[0].negative')
NEGATIVEINCREASE=$(echo $DATA | jq '.[0].negativeIncrease')
DEAD=$(echo $DATA | jq '.[0].death')
DEADINCREASE=$(echo $DATA | jq '.[0].deathIncrease')
HOSPITALIZED=$(echo $DATA | jq '.[0].hospitalizedCurrently')
TODAY=$(date)

echo "On $TODAY, there were $POSITIVE positive COVID cases which is $POSITIVEINCREASE more than yesterday, $NEGATIVE negative COVID tests which is $NEGATIVEINCREASE more than yesterday, $DEAD that have dies which is $DEADINCREASE more than yesterday, and $HOSPITALIZED currently in the hospital."
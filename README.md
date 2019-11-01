# DSlab9
```rs0:PRIMARY> rs.status()
{
  "set" : "rs0",
  "date" : ISODate("2019-11-01T21:02:16.556Z"),
  "myState" : 1,
  "term" : NumberLong(1),
  "syncingTo" : "",
  "syncSourceHost" : "",
  "syncSourceId" : -1,
  "heartbeatIntervalMillis" : NumberLong(2000),
  "majorityVoteCount" : 2,
  "writeMajorityCount" : 2,
  "optimes" : {
    "lastCommittedOpTime" : {
      "ts" : Timestamp(1572642129, 1),
      "t" : NumberLong(1)
    },
    "lastCommittedWallTime" : ISODate("2019-11-01T21:02:09.265Z"),
    "readConcernMajorityOpTime" : {
      "ts" : Timestamp(1572642129, 1),
      "t" : NumberLong(1)
    },
    "readConcernMajorityWallTime" : ISODate("2019-11-01T21:02:09.265Z"),
    "appliedOpTime" : {
      "ts" : Timestamp(1572642129, 1),
      "t" : NumberLong(1)
    },
    "durableOpTime" : {
      "ts" : Timestamp(1572642129, 1),
      "t" : NumberLong(1)
    },
    "lastAppliedWallTime" : ISODate("2019-11-01T21:02:09.265Z"),
    "lastDurableWallTime" : ISODate("2019-11-01T21:02:09.265Z")
  },
  "lastStableRecoveryTimestamp" : Timestamp(1572642089, 1),
  "lastStableCheckpointTimestamp" : Timestamp(1572642089, 1),
  "electionCandidateMetrics" : {
    "lastElectionReason" : "electionTimeout",
    "lastElectionDate" : ISODate("2019-11-01T20:04:28.804Z"),
    "termAtElection" : NumberLong(1),
    "lastCommittedOpTimeAtElection" : {
      "ts" : Timestamp(0, 0),
      "t" : NumberLong(-1)
    },
    "lastSeenOpTimeAtElection" : {
      "ts" : Timestamp(1572638658, 1),
      "t" : NumberLong(-1)
    },
    "numVotesNeeded" : 2,
    "priorityAtElection" : 1,
    "electionTimeoutMillis" : NumberLong(10000),
    "numCatchUpOps" : NumberLong(27017),
    "newTermStartDate" : ISODate("2019-11-01T20:04:29.167Z"),
    "wMajorityWriteAvailabilityDate" : ISODate("2019-11-01T20:04:30.047Z")
  },
  "members" : [
    {
      "_id" : 0,
      "name" : "172.31.43.47:27017",
      "ip" : "172.31.43.47",
      "health" : 1,
      "state" : 1,
      "stateStr" : "PRIMARY",
      "uptime" : 3688,
      "optime" : {
        "ts" : Timestamp(1572642129, 1),
        "t" : NumberLong(1)
      },
      "optimeDate" : ISODate("2019-11-01T21:02:09Z"),
      "syncingTo" : "",
      "syncSourceHost" : "",
      "syncSourceId" : -1,
      "infoMessage" : "",
      "electionTime" : Timestamp(1572638668, 1),
      "electionDate" : ISODate("2019-11-01T20:04:28Z"),
      "configVersion" : 1,
      "self" : true,
      "lastHeartbeatMessage" : ""
    },
    {
      "_id" : 1,
      "name" : "172.31.36.137:27017",
      "ip" : "172.31.36.137",
      "health" : 1,
      "state" : 2,
      "stateStr" : "SECONDARY",
      "uptime" : 3478,
      "optime" : {
        "ts" : Timestamp(1572642129, 1),
        "t" : NumberLong(1)
      },
      "optimeDurable" : {
        "ts" : Timestamp(1572642129, 1),
        "t" : NumberLong(1)
      },
      "optimeDate" : ISODate("2019-11-01T21:02:09Z"),
      "optimeDurableDate" : ISODate("2019-11-01T21:02:09Z"),
      "lastHeartbeat" : ISODate("2019-11-01T21:02:15.474Z"),
      "lastHeartbeatRecv" : ISODate("2019-11-01T21:02:16.380Z"),
      "pingMs" : NumberLong(0),
      "lastHeartbeatMessage" : "",
      "syncingTo" : "172.31.43.47:27017",
      "syncSourceHost" : "172.31.43.47:27017",
      "syncSourceId" : 0,
      "infoMessage" : "",
      "configVersion" : 1
    },
    {
      "_id" : 2,
      "name" : "172.31.38.21:27017",
      "ip" : "172.31.38.21",
      "health" : 1,
      "state" : 2,
      "stateStr" : "SECONDARY",
      "uptime" : 3478,
      "optime" : {
        "ts" : Timestamp(1572642129, 1),
        "t" : NumberLong(1)
      },
      "optimeDurable" : {
        "ts" : Timestamp(1572642129, 1),
        "t" : NumberLong(1)
      },
      "optimeDate" : ISODate("2019-11-01T21:02:09Z"),
      "optimeDurableDate" : ISODate("2019-11-01T21:02:09Z"),
      "lastHeartbeat" : ISODate("2019-11-01T21:02:15.474Z"),
      "lastHeartbeatRecv" : ISODate("2019-11-01T21:02:16.379Z"),
      "pingMs" : NumberLong(0),
      "lastHeartbeatMessage" : "",
      "syncingTo" : "172.31.43.47:27017",
      "syncSourceHost" : "172.31.43.47:27017",

Лиля, [02.11.19 00:02]

      "syncSourceId" : 0,
      "infoMessage" : "",
      "configVersion" : 1
    }
  ],
  "ok" : 1,
  "$clusterTime" : {
    "clusterTime" : Timestamp(1572642129, 1),
    "signature" : {
      "hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
      "keyId" : NumberLong(0)
    }
  },
  "operationTime" : Timestamp(1572642129, 1)
}
rs0:PRIMARY> rs.config()
{
  "_id" : "rs0",
  "version" : 1,
  "protocolVersion" : NumberLong(1),
  "writeConcernMajorityJournalDefault" : true,
  "members" : [
    {
      "_id" : 0,
      "host" : "172.31.43.47:27017",
      "arbiterOnly" : false,
      "buildIndexes" : true,
      "hidden" : false,
      "priority" : 1,
      "tags" : {
        
      },
      "slaveDelay" : NumberLong(0),
      "votes" : 1
    },
    {
      "_id" : 1,
      "host" : "172.31.36.137:27017",
      "arbiterOnly" : false,
      "buildIndexes" : true,
      "hidden" : false,
      "priority" : 1,
      "tags" : {
        
      },
      "slaveDelay" : NumberLong(0),
      "votes" : 1
    },
    {
      "_id" : 2,
      "host" : "172.31.38.21:27017",
      "arbiterOnly" : false,
      "buildIndexes" : true,
      "hidden" : false,
      "priority" : 1,
      "tags" : {
        
      },
      "slaveDelay" : NumberLong(0),
      "votes" : 1
    }
  ],
  "settings" : {
    "chainingAllowed" : true,
    "heartbeatIntervalMillis" : 2000,
    "heartbeatTimeoutSecs" : 10,
    "electionTimeoutMillis" : 10000,
    "catchUpTimeoutMillis" : -1,
    "catchUpTakeoverDelayMillis" : 30000,
    "getLastErrorModes" : {
      
    },
    "getLastErrorDefaults" : {
      "w" : 1,
      "wtimeout" : 0
    },
    "replicaSetId" : ObjectId("5dbc8fc26468c43cff42cb5a")
  }
}
rs0:PRIMARY>```
![Image alt] (https://github.com/vvertash/DSlab9/blob/master/screen1.jpg)

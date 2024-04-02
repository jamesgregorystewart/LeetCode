# Exposition

Where to practice: draw.io

Thoughts on Back of Envelope Estimations:
- as you gather requirements write down estimates for Daily user count, peak user count, read and write queries per second where applicable

Data Types:
- char: 1-4 bytes depending on ASCII or UTF-8; 2 is reasonable
- int: 4 bytes
- bigint: 8 bytes
- timestamp: 8 bytes
- lat/long: 8 bytes each
- seconds in day: 86,400 or 10^5 (100,000)


# This will be a Step by Step Guide of a System Design Interview

Problem Statement: Let's design a system that counts things at scale.

E.g. Counts youtube video views, Likes on Facebook/Instagram.

Maybe we will be asked to generate a set of metrics like application performance metrics in real-time.

Immediate questions from a simple prompt:
- What does data analysis mean?
- Who sends us this data?
- Who uses result of this analysis?
- What does real-time really mean?

## Asking questions

Why is it important? From the interviewer's perspective:
- They want to understand how the candidate deals with ambiguity.
- This quality is important for the daily job

From the Interviewee's perspective:
- We need to make sure we know what the right set of technlogies we need to consider to solve the problem. Let's let the interviewer make the job easier for us by guiding our solution and adding constraints and requirements.

### Requirements Clarification

During requirements clarification, the interviewer starts to understand candidate's level of expertise.

Focus on:
- Users/Customers
- Scale (read and write)
- Performance (how fast)
- Cost

#### Users/Customers questions
- Who will use the system?
    -> all viewers? per hour statistic by owner? machine learning models?
- How the system will be used?
    -> marketing department to generate monthly reports

#### Scale
Should give us an idea of how much data is cooming into the system, and how much data is retrieved from the system.
- How many read queries per second?
- How much data is queried per request?
- How many video views are processed per second?
- Can there be spikes in traffic?

Interviewer will help us define these numbers

#### Performance
Questions in this category should help us quickly evaluate different design options.
- What is expected write-to-read data delay?
    -> can we count views several hours later than these views actually happened? If not, we must consider streaming instead of batch.
- What is expected p99 latency for read queries?
    -> If response time must be as small as possible then we must count views when we write data and do minimal or no counting when reading data. Data must already be aggregated.

#### Cost
- Should we design minimize the cost of development?
    -> If so, we should consider using open-source frameworks.
- Should the design minimize the cost of maintenance?
    -> We should consider public cloud services.


#### Conclusion

Really consider the data. What data? How much data? How fast is the data? Who is using the data? End goal is to get us closer to both functional and non-functional requirements. Functional requirements will be the system behavior, or more specifically APIs (a set of operations a system will support). Non-functional requirements will be qualities of the system -- is it fast, fault-tolerant, secure?

## Functional Requirements

After figuring out what the system has to do, we write it down in a few sentences. For example:
- The system has to count video view events.
    -> count view events is the actual action the system performs and video becomes the input parameter
    `countViewEvent(videoId)`

    If we want to generalize the metric from views to include *likes*, *shares*, etc we can introduce an event type parameter
    `countEvent(videoId, eventType)`

    If we wanted to do more than just count and perform other functions like *count*, *sum*, and *average* 
    `processEvent(videoId, eventType, function)`

    We can generalize further and say that we can process events in batches
    `processEvents(listOfEvents)`

- The system has to return video views count for a time period.
    `getViewsCount(videoId, startTime, endTime)`

    If we want to generalize the event to count
    `getCount(videoId, eventType, startTime, endTime)`

    If we want to generalize the stat 
    `getStats(videoId, eventType, function, startTime, endTime)`


## Non-Functional Requirements

The qualities the system must have. Scalable. Fault-tolerant. Secure. Available. Etc.

The interviewer will not list these directly but will challenge us with mentioning things like "big-scale" and "high-performance" because it is difficult to achieve both at the same time, we will need to find tradeoffs.

- Scalable (tens of thousands of video views per second)
- Highly Performant (few tens of milliseconds to return total views count for a video)
- Highly Available (survives hardware/network failures, no single point of failure)

CAP Theorem tells me I should be choosing between Availability and Consistency. I will go with Availability.

## What We Store

We can store individual events or aggregate data. 

### Individual events

- Fast writes
- Slice and dice data however we need
- Can recalculate numbers if needed

- Slow reads
- Costly for a large scale

### Aggregate Data

- Fast reads
- Data is ready for decision making

- Can query on the way data was aggregated
- Requires data aggregation pipeline
- Hard to impossible to fix errors in the pipeline

### What do we choose

Well we can do both at the cost of more expense, and more complexity. However, this is the best of both worlds.


### Where do we store the data?

- How to scale writes?
- How to scale reads?
- How to make both writes and reads fast?
- How not to lose data in case of hardware faults and network partitions?
- How to achieve strong consistency? What are the tradeoffs?
- How to recoover data in case of an outage?
- How to ensure data security?
- How to make it extensible for data model changes in teh future?
- Where to run? (on-prem or in the cloud?)
- How much money will it all cost?

### SQL Considerations

E.g. Postgres, Vitess

- Shard databases so you add additional machines which take a subset of the data. 
- Cluster proxy will sit in front of all the machines and decide to which machine will the processing service write, or from which will the query service read.

### NoSQL Considerations

E.g. Cassandra

- Shards or "nodes" talk to each other and exchange information about their state. This is called "gossip protocol"


### How We Store the Data?

This is when we dig into the data modelling. 

We want to build a report. We need information about 3 entities: video, number of views per hour for last several hours, and which channel this video belongs to.

In a SQL DB we'll have 3 tables: `Video_Info[video_id][name][...][channel_id]`, `Video_Stats[video_id][timestamp][count]`, and `Channel_Info[channel_id][name]`
We'll run a join query to bring the data from the tables together and normalize it. The tables are denormalized meaning the tables keep the related data apart, which makes changing data later on much easier.

In a NoSQL database we keep all of the data about the videos, their counts, and the channel to which they belong in a single table.

Conclusion on Storage:
- 4 types of NoSQL databases. Cassandra is fault-tolerant, scalable, and read and write throughput increases linearly as machines are added, can replicate across zones, and works well with time series data.  

## Processing service

- How to scale?
- How to achieve high throughput?
- How not to lose data when processing node crashes?
- What to do when database is unavailable or Slow?

Scalable = Partitioning
Reliable = Replication and checkpointing
Fast = In-memory

## Skipped a bunch of stuff....

## After the design is mostly on the board, the functional and nonfunctional requirements have largely been addressed...

Raise points and concerns about 

### How to identify bottlenecks

Testing:
- Load Testing
- Integration Testing
- Smoke Testing

### How to make sure system is healthy

Telemetrics
- Error count
- Log count
- Last LSN, or delta of LSN
- Record row count
- latency
- throughput
- I/O
- Heartbeats that runs to make sure moments of low to no volume are still running

### How to make sure system produces Accurate Results?

E2E Testing
- Great Expectations, DBT
- Send sample record and check if it made it to the end (lower environments)
- 

## SUMMARY

Functional Requirements (API) -> Non-functional Requirements (qualities) -> High-level design -> Detailed Design -> Bottlenecks and tradeoffs

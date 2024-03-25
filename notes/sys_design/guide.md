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
- We need to make sure we know what the right set of technologies we need to consider to solve the problem. Let's let the interviewer make the job easier for us by guiding our solution and adding constraints and requirements.

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

    `getCount(videoId, eventType, startTime, endTime)`

    `getStats(videoId, eventType, function, startTime, endTime)`

# Messaging App Minimum Viable Product

## Why you implemented this way?
I've thought in 3 entities necessary to be able to implement a MVP: User, Messages and Session. 

**User:** Needed to have the information about the users like the name, location of the user and the profile picture. Obviously, I've needed to identity who's the user that is sending a message and to whom.

**Messages**: Effectively, the application purpose is to send out messages from the user A to user B, so I needed an entity that represented a message, with fields like the text content, a timestamp and a session ID (which I'm going to explain next).

**Session**: Finally, a conversation between two users is essentially a session where I keep the value of the user A and user B IDs.

I don't think that I've needed more than these 3 entities to be able to effectively represent a messaging service. The real-time implementation wasn't needed (as a Front-End wasn't necessary) and therefore I've decided to keep it simple enough. If it was necessary a real-time flow of the messages (and the receiving user to be notifed that received a message) I needed to implement RabbitMQ or Redis to be able to flood those same notifications.

I've used FastAPI for the back-end as the requirement indicated that the language of choice was Python, and FastAPI is simple enough to be able to do a quick prototype. For the database I've used PostgreSQL as I'm confortable enough to setup and use a database like it (as well as PostgreSQL supports a big number of tuples, so in principle, should be a scalable solution). For ORM operations, I've used SQLAlchemy as it's the recommended way to do so. To manage the applications installed on the back-end, I've used a virtual environment and set it as the community advise to. Finally, I've used Postman to test out the endpoints.

## What were you planning to do but couldn't complete?
- The Message entity should have at least an ID that represented the one User that sent the message. On Sessions I only keep the relation between the User A and User B that are envolved in a conversation. As the IDs should are interchangable (doesn't matter the order on the Session table), the Message should have that extra piece of message.

- Group messaging should be possible. An entity with an attribute that was a list of IDs should have been implemented, but as the time was limited and some issues were happening with the configuration of the virtual environment, I've decided to adjourn this feature.

- API security. The endpoints for User management are open and shouldn't be, as it's a security flaw. Maybe using a token as a column on the User table was the fix -- this token would only be available for the Admins, or better said, entities that should be able to generate these tokens. Maybe a different table for AdminUsers was needed, with the Foreign Key pointing to the User ID table. Also, as an authentication system was not in place, it was a bit complex and consumed a bit of time to try to implement something of this magnitude.

- The error handling was not the greatest as well. I've should have implemented a better handling of not finding an user on the DB, or a message containing illegal characters, or simply passing a certain number of characters. Also, limiting/cleaning the inputs for exploits like SQL injection to not be possible.

- The profile pictures should have a cloud storage where they were uploaded and retreived as necessary.

## Ideas for future improvments
- Real-time interaction: having a RabbitMQ or a Redis ready and implemented for a real-time flow of sending out messages and receiving notifications. With this, a front-end would be necessary to be developed. This way, the solution would be fully scalable, with maybe with creation of MicroServices to even better up that scenario.

- Deployment on cloud: it is the best way to test out the implementation. This would also imply to have better security (and not having the passwords or connection strings to the database, for instance, exposed on the code).

- Adding Unit Testing, End-to-End and Regression testing, even if the implementation is simple.

- These two aforementioned ideas implied Infrastructure-as-Code to maintain homogeneity between environments and CI/CD for automated deployment/testing.

- Adding a Content Delivery Network to allow the media uploaded into the messaging system to be delivered faster (and having the location of the users would facilitate this subject).
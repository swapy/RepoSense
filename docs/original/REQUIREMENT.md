I am thinking of creating a web app that will scan the input repository given by user and will generate a report based on criterion selected by user.

I want you to digest this idea and refine it.

This is the flow:
1. User lands on our website
2. User selects criterion on which he wants to assess his software and download the document.
3. User will give this document to his ai tool that will assess his repository. 



Lets understand criterion:
Eg: in our day to day development, we have learnings and we end up fixing all our repos to follow a standard eg:
1. repo must have proper tests
2. code coverage
3. proper git setup, gitignore
4. security - no outdated dependencies/vulnerable deps
5. security- no vulnerable code
6. security - weak encryption / hash algorithm usage
7. observability - recording metrics, custom metrics,
8. error handling - standard error framework/standardizing errors with problem json
9. logging - pii masking/data masking
10. Low level design - antipatterns
11. dead code audit

and so on.

Our website will have a document that has prompt for ai per requirement. 
eg: for git setup - we can have a prompt document to check if all required folders only are commited, gitignore is up to date, no git antipatterns.

security- dependency scan - we can have a generic prompt that will do security scan with opensource tools.


So we can have N verticals eg:
1. security 
2. logging
3. version control
4. database management
5. cache management
6. configuration management
7. low level design
8. observability
9. Testing
10. clean code
11. error handling 
12. code coupling/cohesion/cycomatic complexity and so on..
13. ai slop and so on..
14. Ai based practices - eg: if claude, we have claude md, claude settings and so on setup in repo.
15. repository basic info 

each vertical can have sub vertical.
eg: security-  SAST scan/DAST scan , api keys leaks, sensitive info leak, piii leak
observability - metrics, correct logs, correct APM integration, alerting

We can also have a collective eg: prodcution readiness(can have N verticals), architecture,  and so on.

User selects either by vertical, sub vertical or by collective as well. 
If choosing vertical, can choose which sub verticals to cater.



Finally, user can download the criterion based selected items as zip:
Zip contains all prompts in order and a root file which is base promt which will hold all files together to instruct ai on how to scan


For each vertical, subvertical, or even collective we can have following to display on website

1. what this is about
2. description of the item
3. tags
4. What all items it will be looking for.(might be roughly, can vary repo to repo)
5. downloads
6. version(starting v1)

we can see how we can have best practice for versionning as i dont want confusion around versionning or we can totally drop versioning if its too complicated.

We should refine this idea, create proper understanding first.





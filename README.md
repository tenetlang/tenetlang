# tenetlang 🤖💻
> A GPT-Designed Language Built for Humans

See [GPT4 Designed a Programming Language](https://lukebechtel.com/blog/gpt4-generating-code) for some background.

## SEEKING CONTRIBUTORS
I've made lots of neat software, but only one new language before, so I'll need some help to coax GPT in the right directions, and avoid common pitfalls.

Want to help?
- Check the TODO list below
- Read over the blog post & copy the history into ChatGPT, to continue the exploration :)

## TODO / Open Questions
- [ ] How much do we allow for human intervention in the design?
- [ ] How can we not have to copy-paste things into ChatGPT to get good answers (GPT-4 API will solve this, but not everyone has access, and the rate limits are somewhat expensive)
- [ ] Is `GPT-3.5-turbo` good enough for certain subcases, such as writing specific lexers / parsers?


# GPT-4's Original Tenets

While it is difficult to provide a single grand unifying theory of software development, here are ten key tenets that could serve as a comprehensive guide for developing high-quality software:

1. Modularity: Break software into smaller, self-contained, and reusable components to simplify development, maintenance, and understanding.

2. Abstraction: Hide the complexity of the system by providing well-defined interfaces and separating concerns to allow developers to focus on specific areas without being overwhelmed by details.

3. Scalability: Design software to handle a wide range of workloads and demands, with the ability to scale efficiently and effectively as needed.

4. Maintainability: Write clean, understandable, and well-documented code to facilitate easier maintenance, updates, and collaboration.

5. Testability: Develop a comprehensive testing strategy, including unit, integration, and system testing, to ensure the software is robust and reliable.

6. Adaptability: Design software with the flexibility to accommodate future changes, such as updates to requirements, technologies, or user needs.

7. Performance: Optimize software to run efficiently, minimizing resource usage and maximizing response times, without compromising functionality or maintainability.

8. Security: Implement strong security measures to protect software and user data from unauthorized access, misuse, and vulnerabilities.

9. Collaboration: Encourage effective communication and teamwork among developers, testers, designers, and other stakeholders to ensure a shared understanding of project goals, requirements, and progress.

10. Continuous improvement: Embrace a culture of ongoing learning, evaluation, and iterative development to improve the software and development process over time, adapting to new techniques, technologies, and best practices.

Here are some examples of places where the tenets of software development work well in practice and where there are difficulties:

1. Modularity:

    - Works well: Unix philosophy of building small, focused tools that perform one task well (e.g., grep, sed, awk) and can be combined to create complex pipelines.
    - Difficulties: Large legacy systems with tightly coupled components, where it is challenging to refactor or introduce new features without breaking existing functionality.

2. Abstraction:
    - Works well: Object-oriented programming languages (e.g., Java, C++) that encourage encapsulation and hiding implementation details behind well-defined interfaces.
    - Difficulties: Overuse of abstraction can lead to over-engineering, making the code more complex than necessary.

3. Scalability:
    - Works well: Distributed systems like Google's MapReduce or Apache Kafka, which can scale horizontally to accommodate massive amounts of data and users.
    - Difficulties: Monolithic architectures that are not designed for scalability, making it challenging to handle increased workloads without major refactoring.
4. Maintainability:
    - Works well: Open-source projects like Linux or Python that have established coding standards and best practices to facilitate collaboration and long-term maintenance.
    - Difficulties: Proprietary codebases with poor documentation or inconsistent coding styles, making it hard to understand and maintain the code.
5. Testability:
    - Works well: Test-driven development (TDD) methodologies that emphasize writing tests before implementing code, ensuring thorough test coverage and more reliable software.
    - Difficulties: Complex systems with many dependencies or side effects, making it challenging to isolate components for testing.
6. Adaptability:
    - Works well: Microservices architectures, where individual services can be independently updated, scaled, or replaced without affecting the entire system.
    - Difficulties: Rigid, inflexible code that does not follow the Open/Closed Principle, making it difficult to introduce new features or adapt to changing requirements.

7. Performance:
    - Works well: High-performance computing (HPC) systems, where performance is critical and developers optimize code to run efficiently on specialized hardware.
    - Difficulties: Premature optimization that sacrifices code readability and maintainability for marginal performance gains.
8. Security:
    - Works well: Secure software development practices, such as the OWASP Top Ten, that help developers avoid common security vulnerabilities.
    - Difficulties: Insufficient focus on security, leading to software with easily exploitable vulnerabilities, or reliance on outdated technologies with known security flaws.

9. Collaboration:
    - Works well: Agile methodologies, such as Scrum or Kanban, which emphasize teamwork, communication, and iterative development.
    - Difficulties: Disconnected teams working in silos without effective communication, leading to misunderstandings, duplicated work, and delays.
10. Continuous improvement:
    - Works well: DevOps practices, which encourage the integration of development and operations teams to foster a culture of continuous learning and improvement.
    - Difficulties: Organizations that resist change or lack a culture of learning and experimentation, making it difficult to adopt new techniques, technologies, or best practices.


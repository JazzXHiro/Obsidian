	2025-10-08 23:51

Status:

Tags:

---
# OOAD Temp

**1. Object Oriented Analysis** - Process of
	- identifying software eng. requirements
	- and developing software specifications in terms of software system object model
	- comprises of interacting objects
	- requirements are organized around objects which integrate both data and functions
	- key task - identifying and organizing objects, defining their attributes and behaviors, and describing how they interact.

#### Q2: Explain the fundamental concepts of the Object-Oriented paradigm: Objects, Classes, Encapsulation, Inheritance, and Polymorphism.**

**A2:**

- **Object:** An object is a real-world element that can have a physical or conceptual existence. Every object has an identity that distinguishes it from others, a state determined by its properties and their values, and a behavior representing its externally visible activities.
    
- **Class:** A class is a blueprint or description for creating objects. It represents a collection of objects that share the same characteristic properties and common behavior. Creating an object from a class is called instantiation, making an object an "instance" of a class.
    
- **Encapsulation and Data Hiding:** Encapsulation is the process of binding both attributes (data) and methods (functions) together within a class. This allows the internal details of a class to be hidden from the outside, a concept known as data hiding. Data can typically only be accessed through the methods provided by the class interface.
    
- **Inheritance:** Inheritance is a mechanism that allows new classes (subclasses or derived classes) to be created from existing classes (superclasses or base classes). The subclass inherits attributes and methods from the superclass, allowing for code reusability and extension. Inheritance defines an "is-a" relationship.
    
- **Polymorphism:** The word polymorphism means the ability to take multiple forms. In OOAD, it means using operations in different ways depending on the instance they are operating on. It allows objects with different internal structures to have a common external interface, which is particularly effective when implementing inheritance. For example, both a `Circle` and a `Square` class could have a `findArea()` method, but the internal implementation for each would be different.

#### **Q3: What is the Rational Unified Process (RUP)? Explain its four phases.**

**A3:** The Rational Unified Process (RUP) is an iterative software development process framework. It is an adaptable framework intended to be tailored by development organizations. RUP's project life-cycle consists of four distinct phases:

1. **Inception Phase:** The main goal is to adequately scope the system to validate initial costs and budgets. In this phase, a business case, a basic use case model, a project plan, and an initial risk assessment are established. The phase concludes with the **Life Cycle Objective Milestone**, where stakeholders agree on the scope, cost, and schedule estimates.
    
2. **Elaboration Phase:** The primary objective is to mitigate key risks and establish a stable architecture for the project. During this phase, problem domain analysis is performed, and an executable architecture is developed. The use-case model is expected to be about 80% complete. This phase ends with the **Lifecycle Architecture Milestone**, which checks if the product vision and architecture are stable and that major risks are resolved.
    
3. **Construction Phase:** The objective is to build the software system. This phase involves the development of components and other features, and it is where the majority of coding takes place. It concludes with the **Initial Operational Capability Milestone**, marking the first external release of the software.
    
4. **Transition Phase:** The main goal is to transition the system from development into production, making it available to end users. Activities include training end users and maintainers, and beta testing the system against user expectations. The phase ends when the **Product Release Milestone** is reached, and the development cycle is complete.

---
# Reference

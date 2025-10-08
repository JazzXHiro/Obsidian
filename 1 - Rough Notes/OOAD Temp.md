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

#### **Q4: Describe Use Case Diagrams. What is their purpose and how are they drawn?**

**A4:** A use case diagram is a UML diagram that captures the dynamic behavior of a system. It models the system by showing actors, use cases, and the relationships between them.

- **Purpose:**
    
    - To gather the requirements of a system, including internal and external influences.
        
    - To provide an "outside view" of the system.
        
    - To identify external and internal factors that influence the system.
        
    - To show the interactions among requirements and actors.
        
- **How to Draw a Use Case Diagram:**
    
    1. **Identify Functionalities:** These are represented as use cases. The name of a use case should clearly identify the functionality it performs.
        
    2. **Identify Actors:** An actor is something that interacts with the system, such as a human user or another application. Actors should be given suitable names.
        
    3. **Identify Relationships:** Determine the relationships between actors and use cases, and among use cases themselves (e.g., extends, includes).
        
    4. **Define System Boundary:** Draw a boundary box around the use cases to separate the system from the external actors.
     ![[Pasted image 20251009005215.png]]
     ![[Pasted image 20251009005250.png]]
     ![[Pasted image 20251009005331.png]]
     ![[Pasted image 20251009005422.png]]
     ![[Pasted image 20251009005502.png]]
     ![[Pasted image 20251009005546.png]]
1. 

#### **Q5: What are Activity Diagrams? Explain their purpose and key components.**

**A5:** An activity diagram is a flowchart that represents the flow from one activity to another, where an activity can be described as an operation of the system. The diagram can show sequential, branched, and concurrent flows of control.

- **Purpose:**
    
    - To capture the dynamic behavior of a system.
        
    - To model the workflow by showing activities.
        
    - To describe the sequence from one activity to another.
        
    - To provide a high-level understanding of a system's functionalities.
        
- **Key Components (Notations):**
    
    - **Initial State:** The starting point of the process, represented by a solid black circle.
        
    - **Action or Activity State:** Represents the execution of an action, shown as a rectangle with rounded corners.
        
    - **Action Flow (Control Flow):** Shows the transition from one activity to another, represented by a line with an arrowhead.
        
    - **Decision Node:** A diamond shape used to represent a point where the flow of control can branch based on a condition.
        
    - **Fork and Join Nodes:** A solid rectangular bar used to manage concurrent activities. A **Fork** has one incoming flow and splits it into multiple outgoing parallel flows. A **Join** has multiple incoming parallel flows and merges them into a single outgoing flow.
        
    - **Swimlanes:** Used to group related activities into columns or rows, often to represent different actors or departments responsible for those activities.
        
    - **Final State:** The end point of a process, represented by a solid black circle inside another circle.
      ![[Pasted image 20251009011835.png]]
    - 

![[Pasted image 20251009012243.png]]

![[Pasted image 20251009012706.png]]
![[Pasted image 20251009012719.png]]
![[Pasted image 20251009012738.png]]
![[Pasted image 20251009012750.png]]
![[Pasted image 20251009012813.png]]


### Data House vs Data Mart
![[Pasted image 20251009012951.png]]

#### **Q8: Explain the ETL (Extract, Transform, Load) process.**

**A8:** ETL (Extract, Transform, and Load) is a process used in data warehousing to move data from various source systems into a data warehouse. The process consists of three steps:

1. **Extraction:** In this step, data is extracted from the source systems (e.g., Oracle, SQL Server, flat files) and moved into a staging area. Using a staging area prevents the degradation of source system performance and allows data to be validated before it enters the warehouse.
    
2. **Transformation:** The data extracted from the source is often raw and not usable in its original form. In this key step, the data is cleansed, mapped, and transformed by applying calculations, concatenations, or other functions. This process adds value and prepares the data for generating insightful business intelligence reports.
    
3. **Loading:** This is the final step where the transformed data is loaded into the target data warehouse database. Given the huge volume of data that often needs to be loaded in a short time, this process must be optimized for performance.

#### **Q9: What is the KDD (Knowledge Discovery in Data) process?**

**A9:** KDD, also known as Data Mining, is the process of discovering previously unknown relationships and patterns in large datasets. The KDD process involves the following steps:

1. **Data Cleaning:** Noise and inconsistent data are removed.
    
2. **Data Integration:** Multiple data sources are combined into a single dataset.
    
3. **Data Selection:** Data relevant to the specific analysis task is retrieved from the database.
    
4. **Data Transformation:** Data is transformed or consolidated into forms suitable for mining, often through summary or aggregation operations.
    
5. **Data Mining:** Intelligent methods and algorithms are applied to the data to extract patterns.
    
6. **Pattern Evaluation:** The extracted data patterns are evaluated to identify useful information.
    
7. **Knowledge Presentation:** The discovered knowledge is represented and presented to the user, often using visualization techniques or reports.

### Class Diagram

Composition
Aggregation

Based on the provided documents, here is what can be gathered about Class Diagrams.

A **Design Class Diagram** provides a static view of the class definitions within a system. Its primary purpose is to illustrate the attributes and methods of the classes. It is a key diagram used in Domain Modeling and as part of a use-case realization to show participating classes and subsystems.

### Fundamental Components

The core components of a class diagram are classes and the relationships between them.

- **Class:** A class represents a collection of objects that have the same characteristic properties and exhibit common behavior. It serves as a blueprint or description for the objects that can be created from it. A class consists of:
    
    - **Attributes:** A set of properties for the objects instantiated from the class. Attributes are often referred to as class data.
        
    - **Operations (Methods):** A set of operations that portray the behavior of the objects of the class.
        
- **Object:** An object is a real-world element that may have a physical or conceptual existence. It is an instance of a class. Each object has:
    
    - **Identity:** Distinguishes it from other objects.
        
    - **State:** The characteristic properties and the values the object holds.
        
    - **Behavior:** The externally visible activities performed by the object.
        

### Key Relationships and Concepts in Class Diagrams

Class diagrams visually represent several key object-oriented concepts:

- **Inheritance:** This is a mechanism that allows a new class (subclass) to be created from an existing class (superclass). It defines an "is-a" relationship. Testing for systems with inheritance involves checking each derived class, its associations, and aggregations.
    
- **Association:** This represents a relationship between classes. For example, a `Student` class might be associated with a `Course` class.
    
- **Aggregation and Composition:** These are specialized types of association. The documents differentiate between them as a topic for examination questions.
    
- **Multiplicity:** This defines how many instances of one class can be associated with one instance of another class.

![[OOAD Temp 2025-10-09 01.53.44.excalidraw||900]]

#### Q4. Draw a class diagram for the following: A car model has a model name, year, base price, and a manufacturer. Some examples of car models are a 1969 Ford Mustang and a 1975 Volkswagen Rabbit. A physical car has a serial number, color, price, and an owner. As an example of physical cars, John Doe may own a blue Ford with serial number 1FABP and a red Volkswagen with serial number 7E81F.

Classes

**`CarModel`**

This class represents the template or design of a car.

- **Attributes:** `modelName`, `year`, `basePrice`, and `manufacturer`. 

**`PhysicalCar`**

This class represents an actual, specific vehicle.

- **Attributes:** `serialNumber`, `color`, `price`, and `owner`.

**`Manufacturer`**

This class represents the company that produces car models.

- **Attributes:** `name`.

**`Person`**

This class represents an individual who can own a physical car.

- **Attributes:** `name`.

Relationships

**`CarModel` and `Manufacturer`**

- **Relationship:** An association relationship.
- **Description:** A `CarModel` is associated with one `Manufacturer`. A `Manufacturer` can produce many different `CarModel`s.
- **Multiplicity:** The `CarModel` class has a multiplicity of 1 for the `Manufacturer` association. The `Manufacturer` class has a multiplicity of * for the `CarModel` association. 

**`PhysicalCar` and `CarModel`**

- **Relationship:** An association relationship. This is a "type of" relationship, where a specific physical car is an instance of a particular car model.
- **Description:** A `PhysicalCar` is associated with one `CarModel`. A `CarModel` can be instantiated as many different `PhysicalCar`s.
- **Multiplicity:** The `PhysicalCar` class has a multiplicity of 1 for the `CarModel` association. The `CarModel` class has a multiplicity of * for the `PhysicalCar` association. 

**`PhysicalCar` and `Person` (Owner)**

- **Relationship:** An association relationship.
- **Description:** A `PhysicalCar` can be owned by one `Person`. A `Person` can own zero or many `PhysicalCar`s.
- **Multiplicity:** The `PhysicalCar` class has a multiplicity of 1 for the `Person` association. The `Person` class has a multiplicity of 0..* for the `PhysicalCar` association.
![[Pasted image 20251009020356.png]]

## Sequence Diagram



---
# Reference

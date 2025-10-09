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
Sequence diagrams are a type of UML (Unified Modeling Language) diagram that visually represent the interactions between objects or components in a system over time. They focus on the order and timing of messages or events exchanged between different system elements. The diagram captures how objects communicate with each other through a series of messages, providing a clear view of the sequence of operations or processes.

## Sequence Diagram Notations

## ****1. Actors****

An actor in a UML diagram represents a type of role where it interacts with the system and its objects. It is important to note here that an actor is always outside the scope of the system we aim to model using the UML diagram.  

![Actor-11](https://media.geeksforgeeks.org/wp-content/uploads/20240102164916/Actor-11.jpg)

We use actors to depict various roles including human users and other external subjects. We represent an actor in a UML diagram using a stick person notation. We can have multiple actors in a sequence diagram.

### ****For example:****

> Here the user in seat reservation system is shown as an actor where it exists outside the system and is not a part of the system.

![User-interacting-with-seat-reservation-system](https://media.geeksforgeeks.org/wp-content/uploads/20240102164943/User-interacting-with-seat-reservation-system.jpg)

## ****2. Lifelines****

A lifeline is a named element which depicts an individual participant in a sequence diagram. So basically each instance in a sequence diagram is represented by a lifeline. Lifeline elements are located at the top in a sequence diagram. The standard in UML for naming a lifeline follows the following format:

> Instance Name : Class Name

![Sequence-Diagrams](https://media.geeksforgeeks.org/wp-content/uploads/20231228115925/Sequence-Diagrams.jpg)

We display a lifeline in a rectangle called head with its name and type. The head is located on top of a vertical dashed line (referred to as the stem) as shown above.

- If we want to model an unnamed instance, we follow the same pattern except now the portion of lifeline's name is left blank.
- ****Difference between a lifeline and an actor****
    - A lifeline always portrays an object internal to the system whereas actors are used to depict objects external to the system.

The following is an example of a sequence diagram:

![Sequence-Diagram-223](https://media.geeksforgeeks.org/wp-content/uploads/20240102165110/Sequence-Diagram-223.jpg)

## ****3. Messages****

Communication between objects is depicted using messages. The messages appear in a sequential order on the lifeline.

- We represent messages using arrows.
- Lifelines and messages form the core of a sequence diagram.

![Different-Types-of-Messages](https://media.geeksforgeeks.org/wp-content/uploads/20240102165335/Different-Types-of-Messages.jpg)

Messages can be broadly classified into the following categories:

### ****1. Synchronous messages****

A synchronous message waits for a reply before the interaction can move forward. The sender waits until the receiver has completed the processing of the message. The caller continues only when it knows that the receiver has processed the previous message i.e. it receives a reply message.

- A large number of calls in object oriented programming are synchronous.
- We use a ****solid arrow head**** to represent a synchronous message.

![Synchronus-Message-22](https://media.geeksforgeeks.org/wp-content/uploads/20231228132950/Synchronus-Message-22.jpg)

### ****2. Asynchronous Messages****

An asynchronous message does not wait for a reply from the receiver. The interaction moves forward irrespective of the receiver processing the previous message or not. We use a lined arrow head to represent an asynchronous message.

![Asynchronus-Message](https://media.geeksforgeeks.org/wp-content/uploads/20231228134039/Asynchronus-Message.jpg)

## ****4. Create message****

We use a Create message to instantiate a new object in the sequence diagram. There are situations when a particular message call requires the creation of an object. It is represented with a dotted arrow and create word labelled on it to specify that it is the create Message symbol.

****For example:****

> The creation of a new order on a e-commerce website would require a new object of Order class to be created.

![Create-Message](https://media.geeksforgeeks.org/wp-content/uploads/20240102165451/Create-Message.jpg)

## ****5. Delete Message****

We use a Delete Message to delete an object. When an object is deallocated memory or is destroyed within the system we use the Delete Message symbol. It destroys the occurrence of the object in the system.It is represented by an arrow terminating with a x.

****For example:****

> In the scenario below when the order is received by the user, the object of order class can be destroyed.

![Delete-Image](https://media.geeksforgeeks.org/wp-content/uploads/20240102165540/Delete-Image.jpg)

## ****6. Self Message****

Certain scenarios might arise where the object needs to send a message to itself. Such messages are called Self Messages and are represented with a ****U shaped arrow****.

![self-image-1](https://media.geeksforgeeks.org/wp-content/uploads/20231228134413/self-image-1.jpg)

### ****For example:****

> Consider a scenario where the device wants to access its webcam. Such a scenario is represented using a self message.

![Self-Image-2](https://media.geeksforgeeks.org/wp-content/uploads/20231228134633/Self-Image-2.jpg)

## ****7. Reply Message****

Reply messages are used to show the message being sent from the receiver to the sender. We represent a return/reply message using an ****open arrow head with a dotted line****. The interaction moves forward only when a reply message is sent by the receiver.

![Reply-Message](https://media.geeksforgeeks.org/wp-content/uploads/20231228134838/Reply-Message.jpg)

****For example:****

> Consider the scenario where the device requests a photo from the user. Here the message which shows the photo being sent is a reply message.

![Reply-Message-Example](https://media.geeksforgeeks.org/wp-content/uploads/20231228135137/Reply-Message-Example.jpg)

## ****8. Found Message****

A Found message is used to represent a scenario where an unknown source sends the message. It is represented using an ****arrow directed towards a lifeline**** from an end point.

****For example:****

> Consider the scenario of a hardware failure.

![found-message](https://media.geeksforgeeks.org/wp-content/uploads/20240102161203/found-message.jpg)

It can be due to multiple reasons and we are not certain as to what caused the hardware failure.

![found-message-example](https://media.geeksforgeeks.org/wp-content/uploads/20231228135840/found-message-example.jpg)

## ****9. Lost Message****

A Lost message is used to represent a scenario where the recipient is not known to the system. It is represented using an arrow directed towards an end point from a lifeline.

****For example:****

> Consider a scenario where a warning is generated.

![lost-image](https://media.geeksforgeeks.org/wp-content/uploads/20231228140024/lost-image.jpg)

The warning might be generated for the user or other software/object that the lifeline is interacting with. Since the destination is not known before hand, we use the Lost Message symbol.

![Lost-Image-Example](https://media.geeksforgeeks.org/wp-content/uploads/20231228140236/Lost-Image-Example.jpg)

## ****10. Guards****

To model conditions we use guards in UML. They are used when we need to restrict the flow of messages on the pretext of a condition being met. Guards play an important role in letting software developers know the constraints attached to a system or a particular process.

****For example:****

> In order to be able to withdraw cash, having a balance greater than zero is a condition that must be met as shown below.

![Guards](https://media.geeksforgeeks.org/wp-content/uploads/20231228140450/Guards.jpg)

![Example-sequence-diagram-2](https://media.geeksforgeeks.org/wp-content/uploads/20240103162001/Example-sequence-diagram-2.jpg)

## Requirement Engineering

Requirement Engineering is the process of collecting software requirements from a client, then understanding, evaluating, and documenting them1. It serves as a bridge between the initial concept and the subsequent design and construction phases of a project2.

The process of requirement engineering consists of seven distinct tasks:

1. **Inception:** This is the starting task where a set of questions is asked to establish a basic understanding of the problem and to frame a proper solution. It involves collaboration between the developer and the customer to decide the overall scope of the project5.
    
2. **Elicitation:** This task involves finding and gathering the requirements from various sources6.
    
3. **Elaboration:** In this stage, the information gathered during inception and elicitation is expanded and refined7. The primary goal is to develop a pure model of the software that outlines its functions, features, and constraints8.
    
4. **Negotiation:** During this task, the software engineer determines how the project can be achieved with limited business resources9. This includes making rough estimates of development effort and assessing the impact of requirements on the project's cost and delivery time10.
    
5. **Specification:** This task involves constructing the final work product, typically in the form of a Software Requirement Specification (SRS)11. The requirements for the proposed software, including informative, functional, and behavioral aspects, are formalized in both graphical and textual formats12.
    
6. **Validation:** The work product created from the requirement engineering process is assessed for quality13. The primary validation method is conducting formal technical reviews with the software engineer, customer, and other stakeholders14.
    
7. **Requirement Management:** This is a set of activities that helps the project team identify, control, and track requirements and any changes that are made to them during the project15. It begins by assigning a unique identifier to each requirement and then developing a traceability table to manage features, sources, dependencies, and subsystems.


## Aggregation, Generalization and Specialization

### 1. Aggregation

Aggregation is a specialized form of association that models a "has-a" or "part-of" relationship between two classes. It represents a whole-part relationship where the "part" can exist independently of the "whole".

- **Relationship Type:** "Has-A" (e.g., a Team has a Player).
    
- **Key Idea:** It is a **weak** association. The lifecycle of the "part" object is not tied to the lifecycle of the "whole" object. If the "whole" is destroyed, the "part" can still exist.
    
- **Example:** A `Car` and a `Wheel`.
    
    - A `Car` _has_ `Wheels`.
        
    - However, if you scrap the `Car`, the `Wheels` can be removed and can exist on their own, perhaps to be used on another car.
        
- **UML Notation:** A solid line connecting the classes, with an **unfilled (hollow) diamond** on the side of the "whole" class.
    
    (Whole) `Car` <>---- `Wheel` (Part)
    

---

### 2. Generalization

Generalization is the process of extracting shared characteristics (attributes and methods) from two or more classes and combining them into a generalized superclass. It models an "is-a-kind-of" relationship. This is the core principle behind inheritance.

- **Relationship Type:** "Is-A" (e.g., a Car is a Vehicle).
    
- **Key Idea:** It is a **bottom-up** process. You identify commonalities in specific classes (like `Car`, `Truck`) and create a more general parent class (like `Vehicle`). The subclass (child) inherits from the superclass (parent).
    
- **Example:** The classes `Car` and `Truck` both have properties like `speed` and `licensePlate`. We can generalize these into a `Vehicle` superclass.
    
    - `Car` _is a_ `Vehicle`.
        
    - `Truck` _is a_ `Vehicle`.
        
- **UML Notation:** A solid line with a **large, hollow, closed arrowhead** pointing from the specific class (child) to the general class (parent).
    
    `Car` ----▷ `Vehicle`
    

---

### 3. Specialization

Specialization is the reverse process of generalization. It involves creating new, more specific subclasses from an existing general class. The new subclasses inherit the properties of the general class but add their own specific attributes or methods.

- **Relationship Type:** "Is-A" (viewed from the top-down).
    
- **Key Idea:** It is a **top-down** process. You start with a general class (like `Account`) and create more refined, specialized versions (like `SavingsAccount`, `CheckingAccount`). Specialization allows for adding unique features to subclasses.
    
- **Example:** Starting with a `Vehicle` class, you can create specialized subclasses like `Car`, `Motorcycle`, and `Bus`.
    
    - The `Car` class might add a specific attribute like `numberOfDoors`.
        
    - The `Bus` class might add `passengerCapacity`.
        
- **UML Notation:** Uses the **exact same symbol** as generalization. The term simply describes the direction of the design process (i.e., whether you are creating the general class from specifics or the specific classes from the general one).
    
    `SavingsAccount` ----▷ `Account`
    

---

### Summary Table

|Concept|Relationship|Key Idea|Example|
|---|---|---|---|
|**Aggregation**|Has-A|Weak "part-of" link. Part can exist without the whole.|A `Team` has a `Player`.|
|**Generalization**|Is-A|Bottom-up: Creating a parent/superclass from children.|`Car` and `Truck` are generalized into `Vehicle`.|
|**Specialization**|Is-A|Top-down: Creating children/subclasses from a parent.|`Vehicle` is specialized into `Car` and `Truck`.|

---
# Reference

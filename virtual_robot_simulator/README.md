## Method Resolution Order (MRO)
MRO in MaintenanceRobot
When dealing with multiple inheritance in Python, the Method Resolution Order (MRO) determines the order in which base classes are searched when executing a method. Python uses the C3 linearization (or C3 superclass linearization) algorithm to compute the MRO. This ensures a consistent order for method resolution that respects the inheritance hierarchy.

## Impact of MRO on Implementation
In our MaintenanceRobot class, which inherits from both CleaningRobot and CookingRobot, the MRO plays a crucial role in determining how methods and attributes are resolved. The MRO ensures that:

Methods from the immediate superclass (CleaningRobot or CookingRobot) are prioritized based on the order of inheritance.
The super() function calls within the derived classes respect the MRO to avoid redundant initializations or method calls.

## In our implementation:
The multi_task() method in MaintenanceRobot explicitly calls methods from both CleaningRobot and CookingRobot.
We use super() carefully to ensure that __init__ methods from both parent classes are called correctly without conflict.
This structured approach prevents issues such as:

Duplicate initialization of attributes.
Conflicting method calls that could arise from multiple inheritance.
By understanding and leveraging MRO, we ensure that our MaintenanceRobot behaves correctly, performing both cleaning and cooking tasks while maintaining a coherent state and method hierarchy.
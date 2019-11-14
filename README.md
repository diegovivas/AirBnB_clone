## AirBnB clone - The console 
<img src="https://files.realpython.com/media/Working-With-JSON-Data-in-Python_Watermarked.66a8fdcb8859.jpg" align="middle" width="1000" height="700"> 


## Table of Contents
* [Description](#description)
* [File Structure](#file-structure)
* [Requirements](#requirements)
* [Installation](#installation)
* [Usage](#usage)
* [Example of Use](#example-of-use)
* [Bugs](#bugs)
* [Authors](#authors)

## Description
This is a command line interpreter.
Allow manage instances of any classes, serialize and deserialize this instances for create data persistance for the Airbnb program:

Commands:
   ```
   create, show, destroy, all, update.
   ```
Avaible Classes:
   ```
   BaseModel, User, State, Amenity, Place, Review.
   ```

   
## File Structure
* [AUTHORS](AUTHORS) - List of contributors to this repository
* [console.py] - Program command line interpreter
  * `create` - Create a new instance of selected class (ex: create BaseModel)
  * `show` - Prints the string representation of selected instance (ex: BaseModel existing-id)
  * `destroy` - Deletes an instance based on the class name and id (ex: destroy BaseModel 1234-1234-1234)
  * `all` - Prints all string representation of all instances based or not on the class name. (ex:  all BaseModel or $ all. )
  * `update` - Updates an instance based on the class name and id by adding or updating attribute. (ex: update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com") 
* [models/] - Package base, contains all modudes of all classes
  * `amenity.py` - Module with Amenity class
  * `base_model.py` - Module with BaseModel class
  * `city.py` - Module with City class
  * `place.py` - Module with Place class
  * `review.py` - Module with Review class
  * `state.py` - Module with State class
  * `user.py` - Module with User class
  * `engine/` - Package whit file_sorage module
  * `__init__` - Init for the package
* [models/engine/] - Package, contain the file storage module
  * `file_storage.py` - File storage module
  * `__init__` - Init for the package
* [models/base_model.py] - Module with the BaseModel
  * `__init__` - Init attributes of the class
  * `__str__` - Return a specific string format
  * `save` - Update the updated_at attribute and save the instance into json
  * `to_dict` - Create a dictionary representation of de object
* [models/engine/file_storage.py] - Module that serializes and deserializes instences to Json file and vice versa
  * `all` - Return a dictionary with all instances
  * `new` - Save an instance in a dicctionary "__object"
  * `save` - Serialize the dicctionary reprecentation of instances into a json file
  * `reload` - Deserializes the Json file to __objects 
  
 

## Requirements

The console for AirBnb clone is designed to run with `Python 3.4.x` 

## Installation

   - Clone this repository: `git clone "https://github.com/JUCORTESA/AirBnB_clone.git"`
   - Change directories into the repository: `cd AirBnb_clone`
   - Run the console in interactive mode: `./console.py`
   - Or run the console in non-interactive mode: example `echo "<command>" | ./console.py`

## Usage

The console is designed to execute commands in a similar manner to a shell, however with more limited functionality. The development of this consle is ongoing until the command quit is executed. The below features will be checked as they become available:

### Features
- [x] Implementation of storane engine
- [x] Serializacion and Deserialisation with json Files
- [x] Handles command line arguments
- [x] Exit program with quit command or Ctrl + D
- [x] Instances management; "create", "show", "destroy" and "update"
- [x] Count the number of instances of a class
- [x] Quickly use of commands (ex: <class name>.show(<id>))


## Example of Use
Run the executable "console.py" in your terminal:
```
$ ./console.py
(hbnb) all
["[BaseModel] (e1e8068b-8b17-44b8-a63a-339817dda5c2) {'created_at': datetime.datetime(2019, 11, 14, 3, 51, 33, 348610), 'id': 'e1e8068b-8b17-44b8-a63a-339817dda5c2', 'updated_at': datetime.datetime(2019, 11, 14, 3, 51, 33, 348725)}"]
(hbnb)
(hbnb) quit
$
```
## Bugs
At this time, there are no known bugs.

## Authors
Diego Vivas  | [GitHub](https://github.com/diegovivas) | [Twitter](https://twitter.com/rdiegovivas)

Juan Carlos Cortés | [GitHub](https://github.com/jucortesa) | [Twitter](https://twitter.com/jucortesa)


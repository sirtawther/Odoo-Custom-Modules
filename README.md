# Warehouse Transit 

Before using this module, you should create a new transit location for your warehouse in the Odoo Inventory app. Once this is done, you can use this module to hide the default operations types and locations in the Odoo Inventory app when performing transfers, resulting in a more customized user experience.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Download the plugin ZIP file from the repository.
2. Unzip the file to your desired location.
3. Move the extracted files to the `src/user` directory of your Odoo installation.
4. Install the plugin through the Odoo user interface by navigating to `Apps` and searching for the plugin name.

## Usage

1. Create a new transit location for your warehouse in the Odoo Inventory app.
2. Navigate to the Inventory app in Odoo.
3. Select `Operations` from the main menu and then `Transfer`.
4. Click the `Create` button to create a new transfer.
5. In the `Operation Type` field, select the Warehouse Operations Type that corresponds to your needs.
6. In the `Source Location` and `Destination Location` fields, select the transit location you created and the main warehouse, respectively.
7. Replace any default IDs with your own IDs as needed at `views.xml` file. For example, replace the `location_id` field with the ID of your warehouse location.
8. Save the picking and process it as needed.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

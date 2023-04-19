# Odoo-Custom-Modules
After installation and configuration of the views, this module hides the default operations types and locations in the Odoo Inventory app when performing transfers, resulting in a more customized user experience.
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

1. Navigate to the Inventory app in Odoo.
2. Select `Operations` from the main menu and then `Transfer`.
3. Click the `Create` button to create a new transfer.
4. In the `Operation Type` field, select the Warehouse Operations Type that corresponds to your needs.
5. In the `Source Location` and `Destination Location` fields, select the locations that correspond to your warehouse and destination.
6. Replace any default IDs with your own IDs as needed at views.xml file. For example, replace the `location_id` field with the ID of your warehouse location.
7. Save the picking and process it as needed.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

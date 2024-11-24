# Basic Network Sniffer

## Overview

The Basic Network Sniffer project is designed to capture and analyze network traffic. It allows users to monitor network packets in real-time and provides insights into network behavior. This tool can be used for educational purposes, network troubleshooting, and security analysis.

## Features

- Capture live network traffic
- Analyze packet details
- Support for multiple protocols
- Real-time packet filtering
- Export captured data for further analysis

## Installation

### Prerequisites

Ensure that you have the following installed on your machine:

- Python 3.13 or later
- [Install required Python packages](#dependencies)

### Dependencies

To install the necessary Python packages, run:

```bash
pip install -r requirements.txt
```

This will install packages like `numpy`, `pandas`, `requests`, and more.

## Usage

To start capturing packets immediately, you can run the script and see live outputs:

```bash
python main.py
```

If you wish to save captured packets to a CSV file, ensure that the `save_packets_to_file()` function is called in the script:

```python
save_packets_to_file()
``` 

Read the section about the functions in the script to understand how to capture packets live by calling:

```python
capture_from_network()
```

Refer to the function documentation within the code for detailed descriptions.
## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for review.

### Guidelines

1. Ensure code quality and readability.
2. Write clear commit messages.
3. Maintain consistent code style.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Contact

For any questions or suggestions, please reach out to [email@example.com](mailto:email@example.com).

## Acknowledgments

- Inspiration and help received from the community.
- Open-source libraries and tools that made this project possible.# Basic-Network-Sniffer
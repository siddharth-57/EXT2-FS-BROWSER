# Debugfs GUI

Debugfs GUI is a frontend application developed to facilitate reading and navigating through the ext2 filesystem on your computer. It offers a user-friendly interface that allows you to search for files and explore the inode contents of each group, all the way down to the individual blocks. This project aims to provide a comprehensive view of the filesystem structure while maintaining scalability to any block size.

## Features

- **File Search**: Debugfs GUI enables you to search for specific files within the ext2 filesystem. This feature helps you quickly locate and access the desired files.

- **Inode Contents**: Gain insight into the inode contents of each group. Debugfs GUI provides a clear representation of the file metadata, such as permissions, ownership, timestamps, and more.

- **Dynamic Disk Structure**: With its interactive UI, Debugfs GUI dynamically displays the entire disk structure, allowing you to explore and navigate through different levels and directories effortlessly.

- **Scalability**: The application is designed to handle filesystems with varying block sizes. Whether you're working with a small or large block size, Debugfs GUI adapts accordingly, ensuring a seamless experience.

## Technology Stack

The Debugfs GUI project is developed using a combination of Python and C:

- **Python**: The frontend of the application is built using Python, specifically utilizing the Qt5 framework. This choice provides a robust and versatile environment for creating a visually appealing and intuitive user interface.

- **C**: The backend of Debugfs GUI is implemented in C, leveraging its efficiency and low-level access to interact with the ext2 filesystem. The C components work in tandem with the Python frontend to provide a cohesive and reliable user experience.

## Usage

To use Debugfs UI, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies specified in the documentation.
3. Build and run the application using the provided build instructions.
4. Launch Debugfs GUI and begin exploring the ext2 filesystem using the intuitive graphical interface.

Please refer to the detailed documentation for more information on installation, usage, and contributing to the project.

## Contribution

We welcome contributions from the open-source community to enhance and expand the capabilities of Debugfs UI. If you have any ideas, bug fixes, or new features to propose, please follow the guidelines outlined in the contribution documentation.

Let's work together to make Debugfs GUI an even more powerful and user-friendly tool for exploring and understanding the ext2 filesystem!

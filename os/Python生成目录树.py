#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import optparse

LOCATION_NONE     = 'NONE'
LOCATION_MID      = 'MID'
LOCATION_MID_GAP  = 'MID_GAP'
LOCATION_TAIL     = 'TAIL'
LOCATION_TAIL_GAP = 'TAIL_GAP'

Notations = {
    LOCATION_NONE: '',
    LOCATION_MID: '├─',
    LOCATION_MID_GAP: '│  ',
    LOCATION_TAIL: '└─',
    LOCATION_TAIL_GAP: '    '
}

class Node(object):
    def __init__(self, name, depth, parent=None, location=LOCATION_NONE):
        self.name = name
        self.depth = depth
        self.parent = parent
        self.location = location
        self.children = []

    def __str__(self):
        sections = [self.name]
        parent = self.has_parent()
        if parent:
            if self.is_tail():
                sections.insert(0, Notations[LOCATION_TAIL])
            else:
                sections.insert(0, Notations[LOCATION_MID])
            self.__insert_gaps(self, sections)
        return ''.join(sections)

    def __insert_gaps(self, node, sections):
        parent = node.has_parent()
        # parent exists and parent's parent is not the root node
        if parent and parent.has_parent():
            if parent.is_tail():
                sections.insert(0, Notations[LOCATION_TAIL_GAP])
            else:
                sections.insert(0, Notations[LOCATION_MID_GAP])
            self.__insert_gaps(parent, sections)

    def has_parent(self):
        return self.parent

    def has_children(self):
        return self.children

    def add_child(self, node):
        self.children.append(node)

    def is_tail(self):
        return self.location == LOCATION_TAIL

class Tree(object):
    def __init__(self):
        self.nodes = []

    def debug_print(self):
        for node in self.nodes:
            print(str(node) + '/')

    def write2file(self, filename):
        try:
            with open(filename, 'w') as fp:
                fp.writelines(str(node) + '/\n'
                              for node in self.nodes)
        except IOError as e:
            print(e)
            return 0
        return 1

    def build(self, path):
        self.__build(path, 0, None, LOCATION_NONE)

    def __build(self, path, depth, parent, location):
        if os.path.isdir(path):
            name = os.path.basename(path)
            node = Node(name, depth, parent, location)
            self.add_node(node)
            if parent:
                parent.add_child(node)

            entries = self.list_folder(path)
            end_index = len(entries) - 1
            for i, entry in enumerate(entries):
                childpath = os.path.join(path, entry)
                location = LOCATION_TAIL if i == end_index else LOCATION_MID
                self.__build(childpath, depth + 1, node, location)

    def list_folder(self, path):
        """Folders only."""
        return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
        # for entry in os.listdir(path):
        #     childpath = os.path.join(path, entry)
        #     if os.path.isdir(childpath):
        #         yield entry

    def add_node(self, node):
        self.nodes.append(node)

def _parse_args():
    parser = optparse.OptionParser()
    parser.add_option(
        '-p', '--path', dest='path', action='store', type='string',
        default='./', help='the path to generate the tree [default: %default]')
    parser.add_option(
        '-o', '--out', dest='file', action='store', type='string',
        help='the file to save the result [default: pathname.trees]')
    options, args = parser.parse_args()
    # positional arguments are ignored
    return options

def main():
    options = _parse_args()
    path = options.path
    if not os.path.isdir(path):
        print('%s is not a directory' % path)
        return 2

    if not path or path == './':
        filepath = os.path.realpath(__file__)  # for linux
        path = os.path.dirname(filepath)
    tree = Tree()
    tree.build(path)
    # tree.debug_print()
    if options.file:
        filename = options.file
    else:
        name = os.path.basename(path)
        filename = '%s.trees' % name
    return tree.write2file(filename)

if __name__ == '__main__':
    import sys
    sys.exit(main())
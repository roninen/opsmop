
# Generate an RST page

import os

class Index(object):

    def __init__(self, records, dest_dir):

        self.dest_path = os.path.join(dest_dir, 'modules.rst')
        self.records = records

    
    def generate(self):
        self.fd = open(self.dest_path, "w")

        self.fd.write(".. _modules:\n")
        self.fd.write("\n")
        self.fd.write("OpsMop Module Index\n")
        self.fd.write("===================\n")   
        self.fd.write("\n")
        self.fd.write("Available modules by category:\n\n")
        
        categories = self.categories(self.records)

        for category in categories:

            self.fd.write(".. list-table:: %s\n" % category)
            self.fd.write("    :header-rows: 1\n\n")
            self.fd.write("    * - Name\n")
            self.fd.write("      - Purpose\n")
            for record in self.records_for_category(self.records, category):
                self.fd.write("    * - %s\n" % self.gen_rst_link(record))
                self.fd.write("      - %s\n" % record.purpose)

            self.fd.write("\n")
            self.fd.write("\n")

        
        self.fd.write("Hey But What About... ?\n")
        self.fd.write("-----------------------\n")
        self.fd.write("\n")
        self.fd.write("Don't see what you want yet? Opsmop is very new and modules and capabilities are being added all the time!.\n")
        self.fd.write("Your needs matter to us. Think there should be a new module, a new parameter, or want to help build a new provider? You are welcome to stop by the :ref:`forum`.\n")
        self.fd.write("\n")

        self.fd.close()
        print("written: %s" % self.dest_path)

    def categories(self, records):
        return sorted(set([ r.category for r in records ]))

    def records_for_category(self, records, category):
        return [ r for r in records if r.category == category ]

    def gen_rst_link(self, record):
        name = record.name
        return ":ref:`module_%s`" % (record.name)

    
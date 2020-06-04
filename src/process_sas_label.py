import re

file_path = "../data/I94_SAS_Labels_Descriptions.SAS"
head_pattern = re.compile(r"^\s*value\s+\$?(\w+)\s*$")
row_pattern = re.compile(r"^\s*\'?([^=\']+?)\'?\s*=\s*\'?([^\'=]+?)\'?\s*;?\s*$")

out_path = "../output/%s.csv"
if __name__ == "__main__":
    with open(file_path) as f:
        output_file = None
        for line in f:
            r1 = head_pattern.match(line)
            r2 = row_pattern.match(line)
            if r1:
                table_name = r1.group(1)
                print(r1.group(1))
                if output_file != None:
                    output_file.close()
                    output_file = None
                output_file = open(out_path % table_name, "w")
            elif r2:
                if output_file != None:
                    output_file.write("{};{}\n".format(r2.group(1), r2.group(2)))
            if ";" in line and output_file !=None:
                output_file.close()
                output_file = None

        if output_file != None:
            output_file.close()

class IntcodeMachine:

    def __init__(self, _input_string: str):
        self.input_string = _input_string
        self.array_of_ints = _input_string.split(',')
        self.code_map = {}

        for i in range(len(self.array_of_ints)):
            self.code_map[str(i)] = int(self.array_of_ints[i])
        self.machine_state = 0
        self.relative_base = 0
        self.halt = False
        self.input_var = 2
        self.input_used = False
        self.output = []

    def set_input(self, _input: int):
        self.input_var = _input
        self.input_used = False

    def get_from_map(self, _machine_state: int):
        interim = self.code_map.get(str(_machine_state))
        if interim is None:
            interim = 0
        return interim

    def get_instruction_code(self):
        return str(self.get_from_map(self.machine_state))[-1]

    def process_instruction(self, _instruction_code: int):
        instruction = str(self.get_from_map(self.machine_state))

        # print("instruction: " + instruction)
        # print(" ")

        if instruction == "99":
            self.halt = True
        else:
            length_of_instruction = len(instruction)
            dict_of_modes = self.determine_param_modes(instruction, length_of_instruction)
            params_for_calc = self.fetch_inputs(dict_of_modes, _instruction_code)

            if _instruction_code == 1:
                self.process_1(params_for_calc)
            if _instruction_code == 2:
                self.process_2(params_for_calc)
            if _instruction_code == 3:
                self.process_3(params_for_calc)
            if _instruction_code == 4:
                self.process_4(params_for_calc)
            if _instruction_code == 5:
                self.process_5(params_for_calc)
            if _instruction_code == 6:
                self.process_6(params_for_calc)
            if _instruction_code == 7:
                self.process_7(params_for_calc)
            if _instruction_code == 8:
                self.process_8(params_for_calc)
            if _instruction_code == 9:
                self.process_9(params_for_calc)

    def determine_param_modes(self, instruction: str, instruction_length: int) -> dict:
        if instruction_length == 1:
            return {"1": "NORMAL", "2": "NORMAL", "3": "NORMAL"}

        if instruction_length == 3:
            if instruction[0] == "1":
                return {"1": "IMMEDIATE", "2": "NORMAL", "3": "NORMAL"}
            if instruction[0] == "2":
                return {"1": "RELATIVE", "2": "NORMAL", "3": "NORMAL"}

        if instruction_length == 4:
            if instruction[0] == "1":
                if instruction[1] == "1":
                    return {"1": "IMMEDIATE", "2": "IMMEDIATE", "3": "NORMAL"}
                if instruction[1] == "2":
                    return {"1": "RELATIVE", "2": "IMMEDIATE", "3": "NORMAL"}
                if instruction[1] == "0":
                    return {"1": "NORMAL", "2": "IMMEDIATE", "3": "NORMAL"}
            if instruction[0] == "2":
                if instruction[1] == "1":
                    return {"1": "IMMEDIATE", "2": "RELATIVE", "3": "NORMAL"}
                if instruction[1] == "2":
                    return {"1": "RELATIVE", "2": "RELATIVE", "3": "NORMAL"}
                if instruction[1] == "0":
                    return {"1": "NORMAL", "2": "RELATIVE", "3": "NORMAL"}

        if instruction_length == 5:
            if instruction[1] == "1":
                if instruction[2] == "1":
                    return {"1": "IMMEDIATE", "2": "IMMEDIATE", "3": "RELATIVE"}
                if instruction[2] == "2":
                    return {"1": "RELATIVE", "2": "IMMEDIATE", "3": "RELATIVE"}
                if instruction[2] == "0":
                    return {"1": "NORMAL", "2": "IMMEDIATE", "3": "RELATIVE"}
            if instruction[1] == "2":
                if instruction[2] == "1":
                    return {"1": "IMMEDIATE", "2": "RELATIVE", "3": "RELATIVE"}
                if instruction[2] == "2":
                    return {"1": "RELATIVE", "2": "RELATIVE", "3": "RELATIVE"}
                if instruction[2] == "0":
                    return {"1": "NORMAL", "2": "RELATIVE", "3": "RELATIVE"}
            if instruction[1] == "0":
                if instruction[2] == "1":
                    return {"1": "IMMEDIATE", "2": "NORMAL", "3": "RELATIVE"}
                if instruction[2] == "2":
                    return {"1": "RELATIVE", "2": "NORMAL", "3": "RELATIVE"}
                if instruction[2] == "0":
                    return {"1": "NORMAL", "2": "NORMAL", "3": "RELATIVE"}

    def fetch_inputs(self, dict_of_modes: dict, _instruction_code: int) -> dict:
        if _instruction_code == 3:
            return {"param1": self.fetch_output_param(dict_of_modes["1"], self.machine_state + 1), "param2": self.input_var}
        if _instruction_code == 4 or _instruction_code == 9:
            return {"param1": self.fetch_param(dict_of_modes["1"], self.machine_state + 1)}
        if _instruction_code == 5 or _instruction_code == 6:
            return {"param1": self.fetch_param(dict_of_modes["1"], self.machine_state + 1), "param2": self.fetch_param(dict_of_modes["2"], self.machine_state + 2)}

        if _instruction_code == 1 or _instruction_code == 2 or _instruction_code == 7 or _instruction_code == 8:
            return {"param1": self.fetch_param(dict_of_modes["1"], self.machine_state + 1), "param2": self.fetch_param(dict_of_modes["2"], self.machine_state + 2), "param3": self.fetch_output_param(dict_of_modes["3"], self.machine_state + 3)}

    def fetch_param(self, mode: str, place: int) -> int:
        if mode == "NORMAL":
            return self.get_from_map(self.get_from_map(place))
        if mode == "IMMEDIATE":
            return self.get_from_map(place)
        if mode == "RELATIVE":
            return self.get_from_map(self.get_from_map(place) + self.relative_base)

    def fetch_output_param(self, mode: str, place: int) -> int:
        if mode == "NORMAL":
            return self.get_from_map(place)
        if mode == "RELATIVE":
            return self.get_from_map(place) + self.relative_base

    # operation 1 processor
    def process_1(self, params_for_calc: dict):
        self.code_map[str(params_for_calc["param3"])] = params_for_calc["param1"] + params_for_calc["param2"]
        self.machine_state = self.machine_state + 4

    def process_2(self, params_for_calc: dict):
        self.code_map[str(params_for_calc["param3"])] = params_for_calc["param1"] * params_for_calc["param2"]
        self.machine_state = self.machine_state + 4

    def process_3(self, params_for_calc: dict):
        self.code_map[str(params_for_calc["param1"])] = params_for_calc["param2"]
        self.input_used = True
        self.machine_state = self.machine_state + 2

    def process_4(self, params_for_calc: dict):
        self.output.append(params_for_calc["param1"])
        # print("output: " + str(self.output))

        # bespoke functionality
        # self.set_input(self.output)
        # ######
        self.machine_state = self.machine_state + 2

    def process_5(self, params_for_calc: dict):
        if params_for_calc["param1"] == 0:
            self.machine_state = self.machine_state + 3
        else:
            self.machine_state = params_for_calc["param2"]

    def process_6(self, params_for_calc: dict):
        if params_for_calc["param1"] != 0:
            self.machine_state = self.machine_state + 3
        else:
            self.machine_state = params_for_calc["param2"]

    def process_7(self, params_for_calc: dict):
        if params_for_calc["param1"] < params_for_calc["param2"]:
            self.code_map[str(params_for_calc["param3"])] = 1
        else:
            self.code_map[str(params_for_calc["param3"])] = 0
        self.machine_state = self.machine_state + 4

    def process_8(self, params_for_calc: dict):
        if params_for_calc["param1"] == params_for_calc["param2"]:
            self.code_map[str(params_for_calc["param3"])] = 1
        else:
            self.code_map[str(params_for_calc["param3"])] = 0
        self.machine_state = self.machine_state + 4

    def process_9(self, params_for_calc: dict):
        self.relative_base = self.relative_base + params_for_calc["param1"]
        self.machine_state = self.machine_state + 2
	
	def print_output(self):
		

    # # work out parameter settings
    # # put values in
    # .
    # .
    # .
    # .
    # operation 9 processor

    # main intcode program

    def run(self) -> list:
        while not self.halt:
            # print("machine state: " + str(machine_state))
            # print("relative base: " + str(relative_base))
            # print(code_map)
            instruction_code = self.get_instruction_code()
            self.process_instruction(int(instruction_code))
        
        return self.output
        
        
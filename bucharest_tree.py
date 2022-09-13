from config import cities


class BucharestTree:
    def __init__(self) -> None:
        self._initial_point = 'Arad'
        self._final_point = 'Bucharest'
        self.current_point = ''
        self.previews_point = ''
        self.total_distance = 0
        # Cities and paths
        self.registered_paths = []
        self.registered_city = None
        self.all_paths = []
        # second positions
        self.second_positions = ['Zerind', 'Sibiu', 'Timisoara']
        self.second = self.second_positions[0]
        # important intersection point
        self.important_points = ['Fagaras', 'Rimnicu']
        self.intersection_point = self.important_points[0]
        # counters
        self.zerind_count = 0
        self.sibiu_count = 0
        self.timisoara_count = 0
        self.times = 0
        # Boolean variables
        self.is_first_turn = False
        self.paths_completed = False
        self.cities = cities

    def _clear_list(self) -> None:
        self.registered_paths = []

    def _change_intersection_value(self):
        if self.intersection_point == self.important_points[0]:
            self.intersection_point = self.important_points[1]

        elif self.intersection_point == self.important_points[1]:
            self.intersection_point = self.important_points[0]

    def _is_null(self, data: str) -> bool:
        if len(data) == 0 or data == '':
            return True
        return False

    def add_value_to_list(self):
        self.total_distance = self.total_distance - 11
        temp_list = [self.registered_paths, self.total_distance]
        self.all_paths.append(temp_list)

    def check_tree(self):
        while not self.paths_completed:
            for city in self.cities:
                if not self.is_first_turn:
                    if city['proxima'] == self.second:
                        if len(self.registered_paths) == 0:
                            self.registered_city = {
                                'cidade': self._initial_point
                            }
                            self.registered_paths.append(self.registered_city)

                        self.total_distance += city['distancia']
                        self.current_point = city['proxima']
                        self.previews_point = city['anterior']
                        self.registered_city = {
                            'cidade': city['proxima']
                        }
                        self.registered_paths.append(self.registered_city)
                        self.is_first_turn = True
                        break
                else:
                    if self.previews_point == 'Sibiu':
                        self.total_distance += city['distancia']
                        self.current_point = city['proxima']
                        self.previews_point = city['anterior']
                        self.registered_city = {
                            'cidade': city['proxima'],
                        }
                        self.registered_paths.append(self.registered_city)

                    elif city['anterior'] == self.current_point and not city['proxima'] == self.intersection_point:
                        self.total_distance += city['distancia']
                        self.current_point = city['proxima']
                        self.previews_point = city['anterior']
                        self.registered_city = {
                            'cidade': city['proxima'],
                        }
                        self.registered_paths.append(self.registered_city)

                    if self.current_point == self._final_point:
                        if self.sibiu_count == 0 and self.zerind_count == 0:
                            self.add_value_to_list()
                            self._change_intersection_value()
                            self._clear_list()
                            self.sibiu_count += 1
                            self.total_distance = 0
                            self.is_first_turn = False
                            self.current_point = ''
                            self.previews_point = ''
                            break

                        if self.sibiu_count == 1 and self.zerind_count == 0:
                            self.add_value_to_list()
                            self.second = self.second_positions[1]
                            self._change_intersection_value()
                            self._clear_list()
                            self.sibiu_count += 1
                            self.total_distance = 0
                            self.is_first_turn = False
                            self.current_point = ''
                            self.previews_point = ''
                            break

                        if self.zerind_count == 0 and self.sibiu_count == 2:
                            self.add_value_to_list()
                            self.second = self.second_positions[1]
                            self._change_intersection_value()
                            self._clear_list()
                            self.zerind_count += 1
                            self.total_distance = 0
                            self.is_first_turn = False
                            self.current_point = ''
                            self.previews_point = ''
                            break

                        if self.zerind_count == 1 and self.sibiu_count == 2:
                            self.add_value_to_list()
                            self.second = self.second_positions[2]
                            self._change_intersection_value()
                            self._clear_list()
                            self.zerind_count += 1
                            self.total_distance = 0
                            self.is_first_turn = False
                            self.current_point = ''
                            break

                        if self.zerind_count == 2 and self.sibiu_count == 2:
                            self.add_value_to_list()
                            self._clear_list()
                            self.zerind_count += 1
                            self.total_distance = 0
                            self.is_first_turn = False
                            self.current_point = ''
                            self.paths_completed = True
                            break

        for items in self.all_paths:
            print(items)

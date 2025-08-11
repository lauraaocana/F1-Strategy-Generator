CIRCUITS = {
    'Monaco': {
        'length_km': 3.337,
        'fastest_lap': '1:12.909'
    },
    'Silverstone': {
        'length_km': 5.891,
        'fastest_lap': '1:27.097'
    },
    'Belgium': {
        'length_km': 7.004,
        'fastest_lap': '1:46.286'
    },
    'Spain': {
        'length_km': 4.657,
        'fastest_lap': '1:18.149'
    }
}

STRATEGIES = ('Aggressive', 'Conservative', 'Balanced')


def average_speed(lap_time_str, circuit_length):
    try:
        minutes_str, seconds_str = lap_time_str.split(':')
        total_time_seconds = (float(minutes_str) * 60) + float(seconds_str)
        total_time_hours = total_time_seconds / 3600
        average_speed_kph = circuit_length / total_time_hours
        return round(average_speed_kph, 2)
    except (ValueError, IndexError):
        return None


def generate_strategy(chosen_circuit, chosen_strategy):
    circuit_data = CIRCUITS[chosen_circuit]
    circuit_length = circuit_data['length_km']
    fastest_lap_time = circuit_data['fastest_lap']
    
    target_avg_speed = average_speed(fastest_lap_time, circuit_length)

    recommended_tires = ""
    pit_stops = 0

    if chosen_strategy == 'Aggressive':
        recommended_tires = "Soft -> Medium -> Soft"
        pit_stops = 2
    
    elif chosen_strategy == 'Conservative':
        recommended_tires = "Medium -> Hard"
        pit_stops = 1
        
    elif chosen_strategy == 'Balanced':
        recommended_tires = "Medium -> Medium -> Soft"
        pit_stops = 2
        
    print("\n--- F1 RACE STRATEGY ---")
    print(f"Circuit: {chosen_circuit}")
    print(f"Strategy Type: {chosen_strategy}")
    print(f"Recommended Pit Stops: {pit_stops}")
    print(f"Recommended Tire Plan: {recommended_tires}")
    
    if target_avg_speed is not None:
        print(f"To match the fastest lap pace, the average speed must be {target_avg_speed} km/h.")
    else:
        print("Could not calculate average speed due to an invalid time format.")
    print("------------------------")

# NEW FUNCTION FOR SIMPLER TESTING
def is_valid_choice(choice, options):
    """
    Checks if a user's choice is in the available options.
    """
    return choice in options


def main():
    print("---F1 STRATEGY GENERATOR---")
    
    print("\nAvailable Circuits:", ', '.join(CIRCUITS))
    chosen_circuit = input("Choose a circuit: ")
    if not is_valid_choice(chosen_circuit, CIRCUITS):
        print(f"'{chosen_circuit}' is not an option.")
        return
    
    print("\nAvailable Strategies:", ', '.join(STRATEGIES))
    chosen_strategy = input("Choose a strategy: ")
    if not is_valid_choice(chosen_strategy, STRATEGIES):
        print(f"'{chosen_strategy}' was not found.")
        return
        
    generate_strategy(chosen_circuit, chosen_strategy)


if __name__ == "__main__":
    main()
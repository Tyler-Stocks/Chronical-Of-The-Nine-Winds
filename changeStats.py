from baseStats import playerBaseStats

def changePlayerStats(stats, stat_name, new_value):
  # Find the dictionary in the list that contains the stat with the matching name
  for stat_dict in stats:
    if stat_name in stat_dict:
      # Change the value of the stat
      stat_dict[stat_name] = new_value
      break
  # Return the modified list
  return stats

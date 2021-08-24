def remove_double_quotes_from_teams_alert(alert):
    """Remove double quotes from all the fields"""
    for field in alert.__dict__:
        if field == "extra_annotations" or field == "extra_labels":
            new_inner_map = {}
            for inner_field in alert.__getattribute__(field):
                original_value = alert.__getattribute__(field)[inner_field]
                modified_value = original_value.replace('"', '')
                new_inner_map[inner_field] = modified_value
            alert.__setattr__(field, new_inner_map)
        else:
            original_value = alert.__getattribute__(field)
            modified_value = original_value.replace('"', '')
            alert.__setattr__(field, modified_value)
    return alert

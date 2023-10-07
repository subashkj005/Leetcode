def reformatDate(date):
    months = {
        'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05',
        'Jun': '06', 'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10',
        'Nov': '11', 'Dec': '12'
    }


    full_date = date.split()

    day = full_date[0][:-2]
    month = months[full_date[1]]
    year = full_date[2]

    if len(day) == 1:
        day = '0' + day

    return (f"{year}-{month}-{day}")


print(reformatDate('25th Jan 2010'))
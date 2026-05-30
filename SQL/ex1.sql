SELECT u.full_name, e.title, e.city, e.start_date
FROM Users AS u
INNER JOIN Registrations AS r ON u.user_id = r.user_id
INNER JOIN Events AS e ON r.event_id = e.event_id
WHERE e.status = 'upcoming'
AND u.city = e.city
ORDER BY e.start_date;
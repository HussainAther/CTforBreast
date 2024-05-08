function num_intersections = detect_intersections(lines)
    % lines: n x 4 matrix where each row represents [x1, y1, x2, y2]
    num_intersections = 0;
    for i = 1:size(lines, 1)
        for j = i+1:size(lines, 1)
            if is_intersecting(lines(i, :), lines(j, :))
                num_intersections += 1;
            end
        end
    end
end

function intersect = is_intersecting(line1, line2)
    % line1, line2: 1 x 4 vectors representing [x1, y1, x2, y2]
    x1 = line1(1); y1 = line1(2); x2 = line1(3); y2 = line1(4);
    x3 = line2(1); y3 = line2(2); x4 = line2(3); y4 = line2(4);
    den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4);
    if den == 0
        intersect = false;
    else
        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den;
        u = ((x1 - x3) * (y1 - y2) - (y1 - y3) * (x1 - x2)) / den;
        intersect = (t >= 0 && t <= 1) && (u >= 0 && u <= 1);
    end
end


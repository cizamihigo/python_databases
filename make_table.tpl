%# template to generate HTML
<p> the open items are as follow </p>
<table border="1"/>
%for row in rows:
    <tr>
    %for col in row:
        <td>{{col}}</td>
    %end
    </tr>
%end
</table>
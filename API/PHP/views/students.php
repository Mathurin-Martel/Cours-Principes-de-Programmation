<h1>Liste des étudiants</h1>

<ul>
<?php foreach ($students as $student): ?>
    <li>
        <?= $student['name'] ?> (<?= $student['age']?> ans)
    </li>
<?php endforeach; ?>
</ul>

const data = {
    labels: [
        'Python',
        'Javascript',
        'SQL',
        'Java',
        'Spark',
        'HTML',
        'Others'
    ],
    datasets: [{
        label: 'Team Average',
        data: [
            all_skills.python_xp__avg,
            all_skills.javascript_xp__avg,
            all_skills.sql_xp__avg,
            all_skills.java_xp__avg,
            all_skills.spark_xp__avg,
            all_skills.html_xp__avg,
            all_skills.others_xp__avg,
        ],
        fill: true,
        backgroundColor: 'rgba(255, 99, 132, 0.2)',
        borderColor: 'rgb(255, 99, 132)',
        pointBackgroundColor: 'rgb(255, 99, 132)',
        pointBorderColor: '#fff',
        pointHoverBackgroundColor: '#fff',
        pointHoverBorderColor: 'rgb(255, 99, 132)'
    }, 
    {
        label: 'My Skills',
        data: [
            user_skills.python_xp,
            user_skills.javascript_xp,
            user_skills.sql_xp,
            user_skills.java_xp,
            user_skills.spark_xp,
            user_skills.html_xp,
            user_skills.others_xp,
        ],
        fill: true,
        backgroundColor: 'rgba(54, 162, 235, 0.2)',
        borderColor: 'rgb(54, 162, 235)',
        pointBackgroundColor: 'rgb(54, 162, 235)',
        pointBorderColor: '#fff',
        pointHoverBackgroundColor: '#fff',
        pointHoverBorderColor: 'rgb(54, 162, 235)'
    }]
};

const config = {
    type: 'radar',
    data: data,
    options: {
        elements: {
            line: {
              borderWidth: 3
            }
        }
    },
};

var myChart = new Chart(
    document.getElementById('myChart'),
    config
);
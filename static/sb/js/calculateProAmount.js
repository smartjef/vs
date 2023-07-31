
function calculateProAmount() {
    const academicLevel = document.getElementById('pro-academic_level');
    const period = document.getElementById('pro-period');
    const calculatedProAmount = document.getElementById('pro-calculated-amount');

    const academicProLevelChargeRate = getProAcademicLevelChargeRate(academicLevel.value);
    const periodProRate = getProPeriodRate(period.value);

    if (!isNaN(academicProLevelChargeRate) && !isNaN(periodProRate)) {
        const amount = 10000 * academicProLevelChargeRate * periodProRate;
        calculatedProAmount.textContent = 'Ksh. ' + amount.toFixed(2);
    } else {
        calculatedProAmount.textContent = 'Ksh. 0';
    }
}

function getProAcademicLevelChargeRate(academicLevelId) {
    const academicProLevelOption = document.querySelector(`#pro-academic_level [value="${academicLevelId}"]`);
    if (academicProLevelOption) {
        return parseFloat(academicProLevelOption.getAttribute('data-charge-rate'));
    }
    return NaN;
}

function getProPeriodRate(periodId) {
    const periodProOption = document.querySelector(`#pro-period [value="${periodId}"]`);
    if (periodProOption) {
        return parseFloat(periodProOption.getAttribute('data-rate'));
    }
    return NaN;
}

document.getElementById('pro-academic_level').addEventListener('change', calculateProAmount);
document.getElementById('pro-period').addEventListener('change', calculateProAmount);

calculateProAmount();
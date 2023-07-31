function calculateAssAmount() {
    const academicLevel = document.getElementById("ass-academic_level");
    const period = document.getElementById("ass-period");
    const calculatedAmount = document.getElementById("ass-calculated-amount");

    const academicLevelChargeRate = getAcademicLevelChargeRate(
        academicLevel.value
    );
    const periodRate = getPeriodRate(period.value);

    if (!isNaN(academicLevelChargeRate) && !isNaN(periodRate)) {
        const amount = 300 * academicLevelChargeRate * periodRate;
        calculatedAmount.textContent = "Ksh. " + amount.toFixed(2);
    } else {
        calculatedAmount.textContent = "Ksh. 0";
    }
}

function getAcademicLevelChargeRate(academicLevelId) {
    const academicLevelOption = document.querySelector(
        `#ass-academic_level [value="${academicLevelId}"]`
    );
    if (academicLevelOption) {
        return parseFloat(academicLevelOption.getAttribute("data-charge-rate"));
    }
    return NaN;
}

function getPeriodRate(periodId) {
    const periodOption = document.querySelector(
        `#ass-period [value="${periodId}"]`
    );
    if (periodOption) {
        return parseFloat(periodOption.getAttribute("data-rate"));
    }
    return NaN;
}

document
    .getElementById("ass-academic_level")
    .addEventListener("change", calculateAssAmount);
document
    .getElementById("ass-period")
    .addEventListener("change", calculateAssAmount);

calculateAssAmount();

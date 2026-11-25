function renderPersianFooterDates() {
  document.querySelectorAll('time[data-persian-timezone]').forEach((element) => {
    const date = new Date(element.dateTime);
    if (!Number.isFinite(date.getTime())) return;

    const options = {
      calendar: 'persian',
      numberingSystem: 'arabext',
      timeZone: element.dataset.persianTimezone,
      year: 'numeric',
      month: '2-digit',
      day: '2-digit',
      hour: '2-digit',
      minute: '2-digit',
      second: '2-digit',
      hourCycle: 'h23',
      timeZoneName: 'short',
    };
    try {
      element.textContent = new Intl.DateTimeFormat('fa-IR', options).format(date);
    } catch (error) {
      if (!(error instanceof RangeError)) throw error;
      // Keep the server-provided timestamp if the browser cannot format this timezone.
    }
  });
}

renderPersianFooterDates();
document.addEventListener('htmx:afterSwap', renderPersianFooterDates);
document.addEventListener('htmx:oobAfterSwap', renderPersianFooterDates);
